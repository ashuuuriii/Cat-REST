from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from catboost import CatBoostRegressor
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

# loading the trained model.
model = CatBoostRegressor()
model_path = 'lib/models/model.json'
model.load_model(model_path, format='json')


class PredictPrice(Resource):
    def post(self):
        request.get_json(force=True)
        parser = reqparse.RequestParser()
        parser.add_argument('date')
        parser.add_argument('area')
        parser.add_argument('houses_sold')
        parser.add_argument('no_of_crimes')
        parser.add_argument('borough_flag')

        # parse_args returns a dictionary.
        # catboost does not accept dictionaries as an input so it must first be converted to a dataframe.
        args = [parser.parse_args()]
        data = pd.DataFrame.from_dict(args).iloc[0, :]

        prediction = model.predict(data)

        output = {'predicted_price': round(prediction, 2)}

        return output, 200


api.add_resource(PredictPrice, '/predict_price')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
