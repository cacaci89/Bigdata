from django.shortcuts import render
import pandas as pd

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# ne names
ne_name =['EVENT','FAC','GPE','LANGUAGE','LAW','LOC','NORP','ORG','PERSON','PRODUCT','WORK_OF_ART']
idx2nename = { str(i) : item for i, item in enumerate(ne_name)}

news_categories=['科技','政治', '社會', '生活', '健康', '國際', '汽車', '財經',  '新奇', '運動', '地方','全部']
idx2cate = { str(i) : item for i, item in enumerate(news_categories)}


# load data
# def load_data_toptec():
#     # read df
#     df_toptec = pd.read_csv(
#         'app_top_person/dataset/news_top_allORG_via_ner.csv')
#     # refresh data
#     global data # make data global. It can be used everywhere.
#     data = {}
#     for idx, row in df_toptec.iterrows():
#         data[row['category']] = eval(row['top_keys'])

def load_data_toporg():
    # read data
    df_topNer = pd.read_csv(
         'top_tec/dataset/news_topkey_by_ne_and_category.csv')

    global data
    data = {}
    for idx, row in df_topNer.iterrows():
        ne_row = eval(row['top_keys'])
        cate_wf={}
        for cate_wf_row in ne_row:
            cate_wf[ cate_wf_row[0] ] = cate_wf_row[1]
        data[row['ne_name']]= cate_wf
    return


# Load data first when starting server.
load_data_toporg()

def home(request):
    return render(request, 'top_tec/home.html')


# def api_get_toptec(request):

#     # chart_data, wf_pairs = get_category_topkey("科技", 10) #先做簡單的測試

#     cate = request.POST.get('news_category')
#     topk = request.POST.get('topk')
#     topk = int(topk)
#     #print(cate, topk)

#     chart_data, wf_pairs = get_category_toptec(cate, topk)

#     # print(chart_data)
#     response = {'chart_data':  chart_data,
#                 'wf_pairs': wf_pairs,
#                 }
#     return JsonResponse(response)

@csrf_exempt
def api_get_toptec(request):

    # POST方式取得新聞類別
    cate = request.POST.get('news_category')
    cate = idx2cate[cate]
    print(cate)

    # 取得多少筆關鍵詞
    topk = int(request.POST.get('topk'))

    ner_value = request.POST.get('ner_value')
    print(ner_value)
    ner_value = idx2nename[ner_value]

    print(ner_value, cate, topk)

    responseData = get_category_topkey(ner_value, cate, topk)
    response = {'data': responseData }
    print(response)
    return JsonResponse(response)

# def get_category_toptec(cate, topk):
#     wf_pairs = data[cate][0:topk]
#     words = [w for w, f in wf_pairs]
#     freqs = [f for w, f in wf_pairs]
#     chart_data = {
#         "category": cate,
#         "labels": words,
#         "values": freqs}
#     return chart_data, wf_pairs  # chart_data is for charting

def get_category_topkey(ner_value, cate, topk):

    wf_pairs = data[ner_value][cate][0:topk]

    if wf_pairs == []:
        return []

    words = [w for w, f in wf_pairs]
    freqs = [f for w, f in wf_pairs]

    # Prepare cloud chart data
    # the minimum and maximum frequency of top words
    min_ = wf_pairs[-1][1]  # the last line is smaller
    max_ = wf_pairs[0][1]   # the first frequency value is larger

    textSizeMin = 10
    textSizeMax = 90

    if (min_ != max_):
        max_min_range = max_ - min_

    else:
        max_min_range = len(wf_pairs)
        min_ = min_ - 1

    # cloud chart data
    # using proportional scaling
    clouddata = [{'text':w, 'size':int(textSizeMin+(f - min_)/max_min_range*(textSizeMax-textSizeMin))} for w, f in wf_pairs]

    responseData = {
        "wf_pairs": wf_pairs,
        "data_barchart":{
                        "category": cate,
                        "labels": words,
                        "values": freqs
                        },
        "data_cloud": clouddata}
    return responseData


print("app_news_analysis--類別熱門人物載入成功!")