// Generated from JFK.g4 by ANTLR 4.7.2

import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.TerminalNode;

/**
 * This class provides an empty implementation of {@link JFKListener},
 * which can be extended to create a listener which only needs to handle a subset
 * of the available methods.
 */
public class LLVMActions extends JFKBaseListener {
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterProgram(JFKParser.ProgramContext ctx) {
		// System.out.println("enterProgram");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitProgram(JFKParser.ProgramContext ctx) {
		// System.out.println("exitProgram");
		// System.out.println();
		System.out.println(LLVMGenerator.generate());
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterLine(JFKParser.LineContext ctx) {
		// System.out.println("enterLine");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitLine(JFKParser.LineContext ctx) {
		// System.out.println("exitLine");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterInput(JFKParser.InputContext ctx) {
		// System.out.println("enterInput");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitInput(JFKParser.InputContext ctx) {
		// System.out.println("exitInput");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterOutput(JFKParser.OutputContext ctx) {
		// System.out.println("enterOutput");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitOutput(JFKParser.OutputContext ctx) {
		// System.out.println("exitOutput");
		if (ctx.STRING() != null) {
			String tmp = ctx.STRING().getText(); 
       		tmp = tmp.substring(1, tmp.length()-1);
			LLVMGenerator.output(tmp);
		}
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterAssign(JFKParser.AssignContext ctx) {
		// System.out.println("enterAssign");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitAssign(JFKParser.AssignContext ctx) {
		// System.out.println("exitAssign");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterAdd(JFKParser.AddContext ctx) {
		// System.out.println("enterAdd");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitAdd(JFKParser.AddContext ctx) {
		// System.out.println("exitAdd");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterSub(JFKParser.SubContext ctx) {
		// System.out.println("enterSub");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitSub(JFKParser.SubContext ctx) {
		// System.out.println("exitSub");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterMul(JFKParser.MulContext ctx) {
		// System.out.println("enterMul");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitMul(JFKParser.MulContext ctx) {
		// System.out.println("exitMul");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterDiv(JFKParser.DivContext ctx) {
		// System.out.println("enterDiv");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitDiv(JFKParser.DivContext ctx) {
		// System.out.println("exitDiv");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterMod(JFKParser.ModContext ctx) {
		// System.out.println("enterMod");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitMod(JFKParser.ModContext ctx) {
		// System.out.println("exitMod");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterSingle(JFKParser.SingleContext ctx) {
		// System.out.println("enterSingle");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitSingle(JFKParser.SingleContext ctx) {
		// System.out.println("exitSingle");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterComment(JFKParser.CommentContext ctx) {
		// System.out.println("enterComment");
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitComment(JFKParser.CommentContext ctx) {
		// System.out.println("exitComment");
	 }
	// /**
	//  * {@inheritDoc}
	//  *
	//  * <p>The default implementation does nothing.</p>
	//  */
	// @Override public void enterValue(JFKParser.ValueContext ctx) {
	// 	// System.out.println("enterValue");
	//  }
	// /**
	//  * {@inheritDoc}
	//  *
	//  * <p>The default implementation does nothing.</p>
	//  */
	// @Override public void exitValue(JFKParser.ValueContext ctx) {
	// 	// System.out.println("exitValue");
	//  }

	 @Override public void enterId(JFKParser.IdContext ctx) {
		// System.out.println("enterId");
	 }
	 /**
	  * {@inheritDoc}
	  *
	  * <p>The default implementation does nothing.</p>
	  */
	 @Override public void exitId(JFKParser.IdContext ctx) {
		// System.out.println("exitId");
	 }
	 /**
	  * {@inheritDoc}
	  *
	  * <p>The default implementation does nothing.</p>
	  */
	 @Override public void enterInt(JFKParser.IntContext ctx) {
		// System.out.println("enterInt");
	 }
	 /**
	  * {@inheritDoc}
	  *
	  * <p>The default implementation does nothing.</p>
	  */
	 @Override public void exitInt(JFKParser.IntContext ctx) {
		// System.out.println("exitInt");
	 }
	 /**
	  * {@inheritDoc}
	  *
	  * <p>The default implementation does nothing.</p>
	  */
	 @Override public void enterFloat(JFKParser.FloatContext ctx) {
		// System.out.println("enterFloat");
	 }
	 /**
	  * {@inheritDoc}
	  *
	  * <p>The default implementation does nothing.</p>
	  */
	 @Override public void exitFloat(JFKParser.FloatContext ctx) {
		// System.out.println("exitFloat");
	 }

	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterEveryRule(ParserRuleContext ctx) {
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitEveryRule(ParserRuleContext ctx) {
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void visitTerminal(TerminalNode node) { }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void visitErrorNode(ErrorNode node) { }
}