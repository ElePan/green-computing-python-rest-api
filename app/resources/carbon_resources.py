
from flask_restful import Resource
from codecarbon import EmissionsTracker
from codecarbon import track_emissions

class HealthResource(Resource):
    @track_emissions
    def get(self):
        print('We track the emission of all the command of the endpoint')
        return 200


class PartialTrackResource(Resource):
    def get(self):
        tracked_list = []
        for i in range(1_000_000):
            tracked_list.append(i)
        print('Non tracked operations: Added 1_000_000 to a list')

        with EmissionsTracker() as tracker:
            print('We track the emission only of the commands inside the tracker')
            tracked_list = []
            for i in range(1_000_000):
                tracked_list.append(i)
            print('Tracked operations: Added 1_000_000 to a list')
        return 204


class EndpointTrackResource(Resource):
    @track_emissions
    def get(self):
        print('We track the emission of all the command of the endpoint')
        numeric_list = []
        for i in range(1_000_000):
            numeric_list.append(i)
        print('Added 1_000_000 to a list')
        return 204
