abstract class Veiculo{
  int qtdPortas;
  abstract void exibePortas();
}

class Carro extends Veiculo{
  void exibePortas(){
      qtdPortas = 4;
      System.out.println("Carro::qtdPortas = " + qtdPortas);
  }
}

class Moto extends Veiculo{
  void exibePortas(){
      qtdPortas = 0;
      System.out.println("Moto::qtdPortas = " + qtdPortas);
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
    Veiculo v[] = { new Moto(), new Moto(), new Carro() };
    
    for (Veiculo veiculo : v) { // LSP
      veiculo.exibePortas();
    }
  }
}
