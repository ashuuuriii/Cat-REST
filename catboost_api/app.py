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

# hash table of boroughs generate a borough flag from depending on the area chosen.
borough = areas = {'barking and dagenham': True, 'barnet': True, 'bexley': True, 'brent': True,
                   'bromley': True, 'camden': True, 'croydon': True, 'ealing': True, 'enfield': True,
                   'tower hamlets': True, 'greenwich': True, 'hackney': True, 'hammersmith and fulham': True,
                   'haringey': True, 'harrow': True, 'havering': True, 'hillingdon': True, 'hounslow': True,
                   'islington': True, 'kensington and chelsea': True, 'kingston upon thames': True,
                   'lambeth': True, 'lewisham': True, 'merton': True, 'newham': True, 'redbridge': True,
                   'richmond upon thames': True, 'southwark': True, 'sutton': True, 'waltham forest': True,
                   'wandsworth': True, 'westminster': True, 'inner london': True, 'outer london': True,
                   'london': True}


class PredictPrice(Resource):
    def post(self):
        request.get_json(force=True)
        parser = reqparse.RequestParser()
        parser.add_argument('date')
        parser.add_argument('area')
        parser.add_argument('houses_sold')
        parser.add_argument('no_of_crimes')

        # parse_args returns a dictionary-like object.
        # catboost does not accept dictionaries as an input so it must first be converted to a dataframe.
        args = parser.parse_args()
        args['borough_flag'] = 1 if borough.get(args['area']) else 0
        data = pd.DataFrame.from_dict([args]).iloc[0, :]

        prediction = model.predict(data)

        output = {'predicted_price': round(prediction, 2)}

        return output, 200


api.add_resource(PredictPrice, '/predict_price')

if __name__ == '__main__':
    app.run()
