from reminder import set_reminder

print("=" * 55)
print("🔔 Reminder Test")
print("=" * 55)

message = input("Enter Reminder : ")
seconds = int(input("Reminder After (seconds): "))

thread = set_reminder(message, seconds)

print("\n✅ Reminder Set Successfully!")
print("Waiting for reminder...\n")

thread.join()

print("\n✅ Reminder Delivered Successfully!")
print("👋 Exiting Program...")