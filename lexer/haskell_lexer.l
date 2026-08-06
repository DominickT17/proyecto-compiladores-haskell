%option noyywrap yylineno

%{
#include <stdio.h>
#include <stdlib.h>

/* Contadores de categorías léxicas. */
static long total_enteros = 0;
static long total_flotantes = 0;
static long total_identificadores = 0;
static long total_booleanos = 0;
static long total_operadores = 0;

/* Muestra el tipo de token, el lexema y la línea. */
static void mostrar_token(const char *tipo, const char *lexema)
{
    printf("%-22s %-25s %d\n", tipo, lexema, yylineno);
}

/* Registra e imprime un operador encontrado. */
static void mostrar_operador(const char *tipo, const char *lexema)
{
    total_operadores++;
    mostrar_token(tipo, lexema);
}

/* Cuenta las líneas y caracteres del archivo. */
static void contar_lineas_y_caracteres(
    FILE *archivo,
    long *lineas,
    long *caracteres
)
{
    int caracter;
    int ultimo_caracter = '\0';

    *lineas = 0;
    *caracteres = 0;

    while ((caracter = fgetc(archivo)) != EOF)
{
    unsigned char valor = (unsigned char) caracter;

    /* Cuenta cada carácter UTF-8 una sola vez. */
    if ((valor & 0xC0) != 0x80)
    {
        (*caracteres)++;
    }

    if (caracter == '\n')
    {
        (*lineas)++;
    }

    ultimo_caracter = caracter;
}

    /* Cuenta la última línea si no termina con salto de línea. */
    if (*caracteres > 0 && ultimo_caracter != '\n')
    {
        (*lineas)++;
    }

    rewind(archivo);
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

DECIMAL             {DIGITO}+"."{DIGITO}+
CARACTER            \'([^\\'\n]|\\.)\'
BOOLEANO            (True|False)

%%

    /* Palabras reservadas de Haskell. */
"case"      { mostrar_token("PR_CASE", yytext); }
"class"     { mostrar_token("PR_CLASS", yytext); }
"data"      { mostrar_token("PR_DATA", yytext); }
"default"   { mostrar_token("PR_DEFAULT", yytext); }
"deriving"  { mostrar_token("PR_DERIVING", yytext); }
"do"        { mostrar_token("PR_DO", yytext); }
"else"      { mostrar_token("PR_ELSE", yytext); }
"foreign"   { mostrar_token("PR_FOREIGN", yytext); }
"if"        { mostrar_token("PR_IF", yytext); }
"import"    { mostrar_token("PR_IMPORT", yytext); }
"in"        { mostrar_token("PR_IN", yytext); }
"infix"     { mostrar_token("PR_INFIX", yytext); }
"infixl"    { mostrar_token("PR_INFIXL", yytext); }
"infixr"    { mostrar_token("PR_INFIXR", yytext); }
"instance"  { mostrar_token("PR_INSTANCE", yytext); }
"let"       { mostrar_token("PR_LET", yytext); }
"module"    { mostrar_token("PR_MODULE", yytext); }
"newtype"   { mostrar_token("PR_NEWTYPE", yytext); }
"of"        { mostrar_token("PR_OF", yytext); }
"then"      { mostrar_token("PR_THEN", yytext); }
"type"      { mostrar_token("PR_TYPE", yytext); }
"where"     { mostrar_token("PR_WHERE", yytext); }
"_"         { mostrar_token("PR_COMODIN", yytext); }

    /* Palabras especiales usadas en importaciones. */
"as"        { mostrar_token("KW_AS", yytext); }
"qualified" { mostrar_token("KW_QUALIFIED", yytext); }
"hiding"    { mostrar_token("KW_HIDING", yytext); }

{COMENTARIO_LINEA} {
    mostrar_token("COMENTARIO", yytext);
}

{CADENA} {
    mostrar_token("CADENA", yytext);
}

    /* Operadores de varios caracteres. */
">=" { mostrar_operador("OP_MAYOR_IGUAL", yytext); }
"<=" { mostrar_operador("OP_MENOR_IGUAL", yytext); }
"==" { mostrar_operador("OP_IGUALDAD", yytext); }
"/=" { mostrar_operador("OP_DIFERENTE", yytext); }
"&&" { mostrar_operador("OP_AND", yytext); }
"||" { mostrar_operador("OP_OR", yytext); }
"++" { mostrar_operador("OP_CONCATENAR", yytext); }
"!!" { mostrar_operador("OP_INDICE", yytext); }
"->" { mostrar_operador("OP_FLECHA_DERECHA", yytext); }
"<-" { mostrar_operador("OP_FLECHA_IZQUIERDA", yytext); }
"::" { mostrar_operador("OP_ANOTACION_TIPO", yytext); }

    /* Operadores de un carácter. */
"="  { mostrar_operador("OP_ASIGNACION", yytext); }
"+"  { mostrar_operador("OP_SUMA", yytext); }
"-"  { mostrar_operador("OP_RESTA", yytext); }
"*"  { mostrar_operador("OP_MULTIPLICACION", yytext); }
"/"  { mostrar_operador("OP_DIVISION", yytext); }
"^"  { mostrar_operador("OP_POTENCIA", yytext); }
">"  { mostrar_operador("OP_MAYOR", yytext); }
"<"  { mostrar_operador("OP_MENOR", yytext); }

    /* Símbolos de agrupación. */
"(" { mostrar_token("PARENTESIS_ABRE", yytext); }
")" { mostrar_token("PARENTESIS_CIERRA", yytext); }
"[" { mostrar_token("CORCHETE_ABRE", yytext); }
"]" { mostrar_token("CORCHETE_CIERRA", yytext); }
"{" { mostrar_token("LLAVE_ABRE", yytext); }
"}" { mostrar_token("LLAVE_CIERRA", yytext); }

    /* Separadores. */
"," { mostrar_token("SEPARADOR_COMA", yytext); }
";" { mostrar_token("SEPARADOR_PUNTO_COMA", yytext); }

{ENTERO} {
    total_enteros++;
    mostrar_token("ENTERO", yytext);
}

{IDENTIFICADOR} {
    total_identificadores++;
    mostrar_token("IDENTIFICADOR", yytext);
}

{BOOLEANO} {
    total_booleanos++;
    mostrar_token("BOOLEANO", yytext);
}

{DECIMAL} {
    total_flotantes++;
    mostrar_token("DECIMAL", yytext);
}

{CARACTER} {
    mostrar_token("CARACTER", yytext);
}

{CONSTRUCTOR} {
    total_identificadores++;
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
    long total_lineas;
    long total_caracteres;

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

    contar_lineas_y_caracteres(
    archivo,
    &total_lineas,
    &total_caracteres
);

    yyin = archivo;

    printf("%-22s %-25s %s\n", "TOKEN", "LEXEMA", "LINEA");
    printf("----------------------------------------------------------------\n");

    yylex();

printf("\nRESUMEN DEL ARCHIVO\n");
printf("-------------------\n");
printf("Lineas: %ld\n", total_lineas);
printf("Caracteres: %ld\n", total_caracteres);
printf("Enteros: %ld\n", total_enteros);
printf("Flotantes: %ld\n", total_flotantes);
printf("Identificadores: %ld\n", total_identificadores);
printf("Booleanos: %ld\n", total_booleanos);
printf("Operadores: %ld\n", total_operadores);

    fclose(archivo);

    return 0;
}