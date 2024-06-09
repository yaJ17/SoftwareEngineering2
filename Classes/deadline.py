from datetime import datetime

class Deadline:
    # counter for id
    id_counter = 0

    # Initializing the Deadline class
    def __init__(self):
        self.deadline = None 
        self.reminder = ""
        self.title = ""
        self.id = None

    # setting the deadline
    # year, month, day are required
    # setting the default time to 11:59:59 pm
    # reminder & title default to blank
    def createDeadline(self, year, month, day, hour=23, minute=59, second=59,  reminder="", title=""):
        self.id = Deadline.id_counter
        self.deadline = datetime(year, month, day, hour, minute, second)
        self.reminder = reminder
        self.title = title


    #check if the current deadline has passed
    def isOverdue(self):
        return datetime.now() > self.deadline

    #check if current deadline is equal to another deadline
    def isEqual(self, other):
        return self.deadline == other.deadline

    #default format of printing the deadline class
    def __str__(self):
        if self.deadline is not None:
            return self.deadline.strftime("%Y-%m-%d %H:%M:%S")
        return ("No Deadline Yet")
    
    
    #setting the individual attributes
    def setDeadline(self, id, year, month, day, hour=11, minutes=59, second=59):
        if (self.id == id):
            self.deadline = datetime(year, month, day, hour, minutes, second)
        else:
            return "ID is nout found"

    def setReminder(self, reminder):
        self.reminder = reminder

    def setTitle(self, title):
        self.title = title

    #getting the individual attributes
    def getReminder(self):
        return self.reminder

    def getTitle(self):
        return self.title
    
    def getID(self):
        return self.id



class DeadlineManager:
    def __init__(self) -> None:
        self.deadlines = {}
        self.next_id = 1
    
    def add_deadline(self, year, month, day, hour=0, minute=0, second=0,  reminder="", title=""):
        deadline = Deadline()
        deadline.createDeadline(year, month, day, hour, minute, second, reminder, title)
        self.deadlines[self.next_id] = deadline
        self.next_id +=1

    def delete_deadline(self, deadline_id):
        for deadline in self.deadlines:
            if deadline.id == deadline_id:
                self.deadlines.remove(deadline)
    
    def __str__(self):
        output = ""
        for deadline_id, deadline in self.deadlines.items():
            output += f"ID: {deadline_id}, Deadline: {str(deadline)}, Reminder: {deadline.reminder}, Title: {deadline.title}\n"
        return output

