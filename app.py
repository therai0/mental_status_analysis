
import sys 
from src.exception.exception import CustomeException
from src.pipeline.prediction_pipeline import PredictionPipeline

from flask import Flask,render_template,request




app = Flask("__main__")


preprocessor_path = "./final_model/preprocessor.pkl"
model_path = "./final_model/model.pkl"

@app.route("/",methods=["GET","POST"])
def index():
    try:
        if request.method == "GET":
            return render_template("index.html")
        
        statement = request.form.get("statement")

        if len(statement.strip()) == 0:
            return render_template("index.html",result="Please enter some thing")

        prediction = PredictionPipeline(statement,preprocessor_path,model_path)
        result = prediction.init_prediction()
        return render_template("index.html",result=result,message=statement)
    except Exception as e:
        raise CustomeException(e,sys)



if __name__ == "__main__":
    app.run(debug=True,port=5009)