%option noyywrap yylineno

%{
#include <stdio.h>
#include <stdlib.h>

/* Muestra el tipo de token, el lexema y la línea. */
static void mostrar_token(const char *tipo, const char *lexema)
{
    printf("%-22s %-25s %d\n", tipo, lexema, yylineno);
}
%}

/* Definiciones básicas utilizadas por las reglas. */
DIGITO              [0-9]
LETRA_MINUSCULA     [a-z_]
LETRA_MAYUSCULA     [A-Z]
RESTO_IDENTIFICADOR [a-zA-Z0-9_']
IDENTIFICADOR       {LETRA_MINUSCULA}{RESTO_IDENTIFICADOR}*
CONSTRUCTOR         {LETRA_MAYUSCULA}{RESTO_IDENTIFICADOR}*
ENTERO              {DIGITO}+
CADENA              \"([^\\\n]|\\.)*\"
COMENTARIO_LINEA    "--"[^\n]*

%%

"module"|"where"|"import"|"qualified"|"as"|"hiding"  {
    mostrar_token("PALABRA_RESERVADA", yytext);
}

"data"|"type"|"newtype"|"class"|"instance"|"deriving" {
    mostrar_token("PALABRA_RESERVADA", yytext);
}

"if"|"then"|"else"|"case"|"of"|"let"|"in"|"do" {
    mostrar_token("PALABRA_RESERVADA", yytext);
}

{COMENTARIO_LINEA} {
    mostrar_token("COMENTARIO", yytext);
}

{CADENA} {
    mostrar_token("CADENA", yytext);
}

">="|"<="|"=="|"/="|"->"|"<-"|"::"|"="|"+"|"-"|"*"|"/"|">"|"<" {
    mostrar_token("OPERADOR", yytext);
}

"("|")"|"["|"]"|"{"|"}"|","|";" {
    mostrar_token("SIMBOLO", yytext);
}

{ENTERO} {
    mostrar_token("ENTERO", yytext);
}

{IDENTIFICADOR} {
    mostrar_token("IDENTIFICADOR", yytext);
}

{CONSTRUCTOR} {
    mostrar_token("CONSTRUCTOR", yytext);
}

[ \t\r]+ {
    /* Los espacios no producen tokens. */
}

\n {
    /* yylineno actualiza automáticamente la línea. */
}

. {
    mostrar_token("NO_RECONOCIDO", yytext);
}

%%

int main(int argc, char *argv[])
{
    FILE *archivo;

    if (argc != 2)
    {
        fprintf(stderr, "Uso: %s archivo.hs\n", argv[0]);
        return 1;
    }

    archivo = fopen(argv[1], "r");

    if (archivo == NULL)
    {
        perror("No se pudo abrir el archivo");
        return 1;
    }

    yyin = archivo;

    printf("%-22s %-25s %s\n", "TOKEN", "LEXEMA", "LINEA");
    printf("----------------------------------------------------------------\n");

    yylex();

    fclose(archivo);

    return 0;
}