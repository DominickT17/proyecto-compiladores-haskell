LEXER_SRC=lexer/haskell_lexer.l
LEXER_C=lexer/lex.yy.c
LEXER_BIN=lexer/haskell_lexer

all: lexer

lexer:
	flex -o $(LEXER_C) $(LEXER_SRC)
	gcc $(LEXER_C) -o $(LEXER_BIN) -lfl

run:
	python gui/app.py

clean:
	rm -f $(LEXER_C) $(LEXER_BIN)