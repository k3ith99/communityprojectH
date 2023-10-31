from flask import Flask, Blueprint, request, json

# from Backend.OpenAI.main import .

itinerary = Blueprint('itinerary', __name__) 

@itinerary.route("/itinerary")
def default():
    return "itinerary"

@itinerary.route("/itinerary_form", methods=['GET', 'POST'])
def get_itinerary():
    try:
        # travel_to = request.form.get('travel-to')
        # travel_from = request.form.get('travel-from')
        # leave_date = request.form.get('leave-date')
        # return_date = request.form.get('return-date')
        # people = request.form.get('people')
        # things_to_note = request.form.get('things-to-note')

        request_data = json.loads(request.data)

        # retrieve item from frontend by request_data['ID']
        print(request_data['travelTo'])

        return {200: "works"}

    except:
        return {404: 'Failed to retreive itinerary data'}

    # return "itinerary"
