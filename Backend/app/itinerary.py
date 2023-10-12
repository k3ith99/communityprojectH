from flask import Flask, Blueprint, request

# from Backend.OpenAI.main import .

itinerary = Blueprint('itinerary', __name__) 

@itinerary.route("/")
def default():
    return "itinerary"

@itinerary.route("/itinerary_form", methods=['GET'])
def get_itinerary():
    try:
        travel_to = request.form.get('travel-to')
        travel_from = request.form.get('travel-from')
        start_date = request.form.get('start-date')
        end_date = request.form.get('end-date')
        people = request.form.get('people')
        things_to_note = request.form.get('things-to-note')

        print(travel_to)

        return "works"

    except:
        return {404: 'Failed to retreive itinerary data'}

    # return "itinerary"
