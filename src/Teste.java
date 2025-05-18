import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

public class Teste {
    public static void main(String[] args) throws Exception {
        // Cria um PrintStream que usa UTF-8 para saída correta no console
        PrintStream out = new PrintStream(System.out, true, StandardCharsets.UTF_8);
        out.println("Teste de configuração do JDK!");
    }
}
