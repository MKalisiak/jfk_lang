import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ANTLRFileStream input = new ANTLRFileStream(args[0]);

        JFKLexer lexer = new JFKLexer(input);

        CommonTokenStream tokens = new CommonTokenStream(lexer);
        JFKParser parser = new JFKParser(tokens);

        ParseTree tree = parser.program(); 

        //System.out.println(tree.toStringTree(parser));

        ParseTreeWalker walker = new ParseTreeWalker();
        walker.walk(new LLVMActions(), tree);

    }
}