from models.pet import Pet
from models.appointment import Appointment
from models.medical_record import MedicalRecord
from models.feeding_schedule import FeedingSchedule

def main():
    while True:
        print("\n1. Add Pet")
        print("2. View Pets")
        print("3. Update Pet")
        print("4. Delete Pet")
        print("5. Schedule Vet Appointment")
        print("6. Log Medical Record")
        print("7. Set Feeding Schedule")
        print("8. View Appointments for a Pet")
        print("9. View Medical Records for a Pet")
        print("10. View Feeding Schedule for a Pet")
        print("11. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            # Add a pet
            name = input("Enter pet name: ")
            species = input("Enter species: ")
            breed = input("Enter breed: ")
            age = int(input("Enter age: "))
            owner_name = input("Enter owner's name: ")
            pet = Pet(name, species, breed, age, owner_name)
            pet.save()

        elif choice == '2':
            # View all pets
            pets = Pet.view_all()
            if pets:
                for pet in pets:
                    print(f"ID: {pet[0]}, Name: {pet[1]}, Species: {pet[2]}, Breed: {pet[3]}, Age: {pet[4]}, Owner: {pet[5]}")
            else:
                print("No pets found.")

        elif choice == '3':
            # Update a pet
            pet_id = int(input("Enter pet ID: "))
            name = input("Enter new name (leave blank to skip): ")
            species = input("Enter new species (leave blank to skip): ")
            breed = input("Enter new breed (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            owner_name = input("Enter new owner's name (leave blank to skip): ")
            updates = {k: v for k, v in {'name': name, 'species': species, 'breed': breed, 'age': age, 'owner_name': owner_name}.items() if v}
            Pet.update(pet_id, **updates)

        elif choice == '4':
            # Delete a pet
            pet_id = int(input("Enter pet ID to delete: "))
            Pet.delete(pet_id)

        elif choice == '5':
            # Schedule a vet appointment
            pet_id = int(input("Enter pet ID: "))
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            description = input("Enter appointment description: ")
            appointment = Appointment(pet_id, appointment_date, description)
            appointment.schedule()

        elif choice == '6':
            # Log a medical record
            pet_id = int(input("Enter pet ID: "))
            record_date = input("Enter record date (YYYY-MM-DD): ")
            notes = input("Enter medical notes: ")
            medical_record = MedicalRecord(pet_id, record_date, notes)
            medical_record.log()

        elif choice == '7':
            # Set a feeding schedule
            pet_id = int(input("Enter pet ID: "))
            feeding_time = input("Enter feeding time (HH:MM:SS): ")
            food_type = input("Enter food type: ")
            feeding_schedule = FeedingSchedule(pet_id, feeding_time, food_type)
            feeding_schedule.set_schedule()

        elif choice == '8':
            # View appointments for a pet
            pet_id = int(input("Enter pet ID: "))
            appointments = Appointment.view_for_pet(pet_id)
            if appointments:
                for appointment in appointments:
                    print(f"Appointment ID: {appointment[0]}, Date: {appointment[2]}, Description: {appointment[3]}")
            else:
                print("No appointments found for this pet.")

        elif choice == '9':
            # View medical records for a pet
            pet_id = int(input("Enter pet ID: "))
            medical_records = MedicalRecord.view_for_pet(pet_id)
            if medical_records:
                for record in medical_records:
                    print(f"Record ID: {record[0]}, Date: {record[2]}, Notes: {record[3]}")
            else:
                print("No medical records found for this pet.")

        elif choice == '10':
            # View feeding schedule for a pet
            pet_id = int(input("Enter pet ID: "))
            feeding_schedules = FeedingSchedule.view_for_pet(pet_id)
            if feeding_schedules:
                for schedule in feeding_schedules:
                    print(f"Schedule ID: {schedule[0]}, Feeding Time: {schedule[2]}, Food Type: {schedule[3]}")
            else:
                print("No feeding schedule found for this pet.")

        elif choice == '11':
            # Exit the application
            print("Exiting Pet Care Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
