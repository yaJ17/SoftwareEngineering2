from datetime import datetime

class Deadline:
    next_id = 1
    def __init__(self, year, month, day, hour=0, minute=0, second=0,  reminder="", title=""):
        self.id = Deadline.next_id
        Deadline.next_id += 1
        self.deadline = datetime(year, month, day, hour, minute, second)
        self.reminder = reminder
        self.title = title
    

    def has_passed(self):
        return datetime.now() > self.deadline

    def deadline_is_past(self, other):
        return self.deadline < other.deadline

    def deadline_is_equal(self, other):
        return self.deadline == other.deadline

    def __str__(self):
        return self.deadline.strftime("%Y-%m-%d %H:%M:%S")
    
    def get_reminder(self):
        return self.reminder
    
    def set_reminder(self, reminder):
        self.reminder = reminder

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

class DeadlineManager:
    def __init__(self) -> None:
        self.deadlines = []
    
    def add_deadline(self, year, month, day, hour=0, minute=0, second=0,  reminder="", title=""):
        deadline = Deadline(year, month, day, hour, minute, second, reminder, title)
        print(deadline)
        self.deadlines.append(deadline)

    def delete_deadline(self, deadline_id):
        print(deadline_id)
        for deadline in self.deadlines:
            if deadline.id == deadline_id:
                self.deadlines.remove(deadline)
                
    
    def __str__(self):
        output = ""
        for deadline in self.deadlines:
            output += f"ID: {deadline.id}, Deadline: {str(deadline)}, Reminder: {deadline.reminder}, Title: {deadline.title}\n"
        return output

# deadline_manager = DeadlineManager()
# deadline_manager.add_deadline(2024, 3, 15, 12, 30, reminder="Hello", title="PRODUCT A")
# deadline_manager.add_deadline(2024, 3, 15, 12, 40, reminder="Hello", title="PRODUCT B")
# deadline_manager.delete_deadline(2)
# print(deadline_manager)
