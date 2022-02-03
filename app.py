import numpy as np
from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)
pca_pred= pickle.load(open('pca1.pkl','rb'))
scaler_pred= pickle.load(open('scalar.pkl','rb'))
model_pred= pickle.load(open('xgboost_model.pkl','rb'))

@app.route('/predict_api',methods=['POST'])
def predict_api():

    data = request.get_json(force=True)
    print(data)
    prediction= model_pred.predict(pca_pred.transform(scaler_pred.transform([np.array(list(data.values()))])))
    output =str(prediction[0])
    
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)



'''
input data format:

{
                             "having_IP_Address":-1, 
                             "URL_Length":1,
                             "Shortining_Service":1,
                             "double_slash_redirecting":-1,
                             "Prefix_Suffix":-1,
                             "having_Sub_Domain":-1,
                             "SSLfinal_State":-1,
                             "Domain_registeration_length":-1,
                             "Request_URL":1,
                             "URL_of_Anchor":-1,
                             "Links_in_tags":1,
                             "SFH":-1,
                             "Abnormal_URL":-1,
                             "Redirect":0,
                             "RightClick":1,
                             "age_of_domain":-1,
                             "DNSRecord":-1,
                             "web_traffic":-1,
                             "Page_Rank":-1,
                             "Google_Index":1,
                             "Links_pointing_to_page":1                         
}

'''