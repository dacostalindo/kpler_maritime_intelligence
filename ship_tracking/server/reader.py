import sqlalchemy
import csv







if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    


def add_csv_to_DB():
    with open('vessel_data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        counter = 1
        for entry in csv_reader:
            ## TODO : Check if latitude, longitude, and time follow physical constraints
            # and if values already exist
            try:
                vessel = VesselModel(id = counter,
                                    vessel_id=int(entry['vessel_id']), 
                                    latitude=float(entry[' latitude']), 
                                    longitude=float(entry[' longitude']), 
                                    time=datetime.strptime(entry[' received_time_utc'], "%Y-%m-%d %H:%M:%S.%f"))
                
                duplicate_entry = VesselModel.query.filter_by(vessel_id=int(entry['vessel_id']),
                                                            latitude=float(entry[' latitude']), 
                                                            longitude=float(entry[' longitude']), 
                                                            time=datetime.strptime(entry[' received_time_utc'], "%Y-%m-%d %H:%M:%S.%f")).first()
                if not duplicate_entry:
                    db.session.add(vessel)
                    counter = counter + 1
                else:
                    print(duplicate_entry)

            except ValueError as e:
                print(f'Couldnt add the {entry} entry - {e}')
            
        if db.session.commit():
            print('Commited the Database successfully')
            
