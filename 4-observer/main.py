
from __future__ import annotations
from abc import ABC, abstractmethod

class BaseSubject(ABC):
  @abstractmethod
  def registerObserver(self):
    pass

  @abstractmethod
  def removeObserver(self):
    pass
  
  @abstractmethod
  def notifyObservers(self):
    pass


class Observer:

  @abstractmethod
  def update(self, sPost):
    pass

class WebsiteSubject(BaseSubject):
    pass

class UserInterface(BaseSubject):
  pass

class Logger(BaseSubject):
  pass


if __name__ == "__main__":
    print("App: ObserverPattern")
    print("\n")
