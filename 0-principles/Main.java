abstract class Veiculo{             // #1. SRP - Single Responsability Principle
  private int qtdPortas = 4;        // o objeto veiculo é responsável por ele mesmo, 
                                    // ou seja, ele define um Veiculo e nada mais
                                    
                                    //#2. OCP - Encapsulamento proteje o objeto e seus atributos
  abstract void exibePortas();
  // abstract void exibePessoa(); - #1. SRP - perde a coesão
  public void setPortas(int qtdPortas){
    this.qtdPortas = qtdPortas;
  }
  public int getPortas(){ 
    return this.qtdPortas;
  }
}

class Carro extends Veiculo{

  void exibePortas(){
      this.setPortas(4);
      System.out.println("Carro::qtdPortas = " + this.getPortas());
  }
}

class Moto extends Veiculo{
  void exibePortas(){
      // quebra o encapsulamento, viola o princípio #2. OCP - Open-Closed Principle       
      // qtdPortas = 10;
      // System.out.println("Moto::qtdPortas = " + qtdPortas);
  }

  void alteraMarcha(){
    System.out.println("Moto:: alterando a marcha");
  }
}

public class Main{
  public static void main(String a[]){
    // Vetor Polimorfico
    // pode ser de várias formas a partir da classe
    // base - Veiculo, no caso, Moto e Carro
    Veiculo v[] = { new Carro(), new Moto(), new Moto() };
    
    for (Veiculo veiculo : v) { // LSP
      veiculo.exibePortas();
    }
  }
}
