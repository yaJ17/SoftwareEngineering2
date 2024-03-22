class Order:

  def __init__(self) -> None:
    self.order_id = 0
    self.client_id = 0
    self.deadline_id = 0
    self.order_quantity = 0 
    self.order_progress = 0
    self.labor_allocation = 0
    self.order_style = ""

  def __str__(self) -> str:
    return (f"{self.order_id}")
  
  
  # def addOrder(self, order_id: int , client_id: int)
