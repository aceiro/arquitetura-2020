
from __future__ import annotations
from abc import ABC, abstractmethod

# Esse código é baseado no modelo do exemplo do seguinte link
# https://android.jlelse.eu/observer-pattern-how-does-it-work-82dfd81305a4
#  
# Desafio - Converter o código Java para Python do Logger e UserInterface observer
# 

# BaseSubject: é uma interface que define os métodos que serão usados 
#              para adicionar, remover e notificar os observers
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


# Observer: são as classes que recebem uma string (post)
#           e atualizam o conteúdo em tela ou em log do usuario
#           por exemplo, o Logger é um Observer
class Observer:

  @abstractmethod
  def update(self, sPost = ""):
    pass

class WebsiteSubject(BaseSubject):
    _observers = []
    _post = ""
    def setData(self, sPost):
      self._post = sPost
      self.notifyObservers()

    def registerObserver(self, observer):
      self._observers.append(observer)

    def removeObserver(self, observer):
      self._observers.remove(observer)
  
    def notifyObservers(self):
      for observer in self._observers:
        observer.update(self._post)

class UserInterface(Observer):
  #2. adicionar as outras implementações para o UserInterface
  def update(self, sPost):
    pass

# Logger: É um observer que implementa o método update()
class Logger(Observer):
  _post = ""
  _subject = None

  def __init__(self):
    super().__init__()

  def __init__(self, subject):
    super().__init__()
    _subject = subject

  def log(self, sPost):
      print("Logger : New post " + sPost)

  def update(self, sPost):
    self._post = sPost
    self.log(self._post)


if __name__ == "__main__":
    print("App: ObserverPattern")
    print("\n")
    print("Logger")
    print("\n")
    
    subject = WebsiteSubject()
    logger  = Logger(subject)
    subject.registerObserver(logger)
    subject.setData("Post 1")

    
    # 1. adicionar outros métodos abstrados 
    #    de referencia ao observer
    #    implementar os @abstractmethod

    # print("WebsiteSubject")
    # print("\n")
    # WebsiteSubject()

    # print("UserInterface")
    # print("\n")
    # UserInterface()
