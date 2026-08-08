%option noyywrap yylineno

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Contadores de categorías léxicas. */
static long total_enteros = 0;
static long total_flotantes = 0;
static long total_identificadores = 0;
static long total_booleanos = 0;
static long total_operadores = 0;

/* Representa un identificador y su número de apariciones. */
typedef struct
{
    char lexema[100];
    long cantidad;
} ConteoIdentificador;

#define MAX_IDENTIFICADORES 200

static ConteoIdentificador identificadores_encontrados[MAX_IDENTIFICADORES];
static size_t cantidad_identificadores_distintos = 0;

/* Representa una palabra reservada y su número de apariciones. */
typedef struct
{
    const char *lexema;
    long cantidad;
} ConteoPalabra;

static ConteoPalabra palabras_reservadas[] =
{
    {"case", 0},
    {"class", 0},
    {"data", 0},
    {"default", 0},
    {"deriving", 0},
    {"do", 0},
    {"else", 0},
    {"foreign", 0},
    {"if", 0},
    {"import", 0},
    {"in", 0},
    {"infix", 0},
    {"infixl", 0},
    {"infixr", 0},
    {"instance", 0},
    {"let", 0},
    {"module", 0},
    {"newtype", 0},
    {"of", 0},
    {"then", 0},
    {"type", 0},
    {"where", 0},
    {"_", 0},
    {"as", 0},
    {"qualified", 0},
    {"hiding", 0}
};

static const size_t total_palabras_reservadas =
    sizeof(palabras_reservadas) / sizeof(palabras_reservadas[0]);

/* Muestra el tipo de token, el lexema y la línea. */
static void mostrar_token(const char *tipo, const char *lexema)
{
    printf("%-22s %-25s %d\n", tipo, lexema, yylineno);
}

/* Registra la aparición de un identificador. */
static void registrar_identificador(const char *lexema)
{
    size_t indice;

    for (indice = 0; indice < cantidad_identificadores_distintos; indice++)
    {
        if (strcmp(identificadores_encontrados[indice].lexema, lexema) == 0)
        {
            identificadores_encontrados[indice].cantidad++;
            return;
        }
    }

    if (cantidad_identificadores_distintos < MAX_IDENTIFICADORES)
    {
        strncpy(
            identificadores_encontrados[cantidad_identificadores_distintos].lexema,
            lexema,
            sizeof(identificadores_encontrados[0].lexema) - 1
        );

        identificadores_encontrados[cantidad_identificadores_distintos]
            .lexema[sizeof(identificadores_encontrados[0].lexema) - 1] = '\0';

        identificadores_encontrados[cantidad_identificadores_distintos].cantidad = 1;
        cantidad_identificadores_distintos++;
    }
}

/* Incrementa el contador de una palabra reservada. */
static void registrar_palabra_reservada(
    const char *tipo,
    const char *lexema
)
{
    size_t indice;

    for (indice = 0; indice < total_palabras_reservadas; indice++)
    {
        if (strcmp(palabras_reservadas[indice].lexema, lexema) == 0)
        {
            palabras_reservadas[indice].cantidad++;
            break;
        }
    }

    mostrar_token(tipo, lexema);
}

/* Ordena por cantidad descendente y después alfabéticamente. */
static int comparar_frecuencias(
    const void *primero,
    const void *segundo
)
{
    const ConteoPalabra *palabra_a =
        (const ConteoPalabra *) primero;

    const ConteoPalabra *palabra_b =
        (const ConteoPalabra *) segundo;

    if (palabra_a->cantidad < palabra_b->cantidad)
    {
        return 1;
    }

    if (palabra_a->cantidad > palabra_b->cantidad)
    {
        return -1;
    }

    return strcmp(palabra_a->lexema, palabra_b->lexema);
}

/* Muestra las palabras encontradas ordenadas por frecuencia. */
static void mostrar_frecuencia_palabras(void)
{
    size_t indice;
    int hay_resultados = 0;

    qsort(
        palabras_reservadas,
        total_palabras_reservadas,
        sizeof(ConteoPalabra),
        comparar_frecuencias
    );

    printf("\nPALABRAS RESERVADAS POR FRECUENCIA\n");
    printf("---------------------------------\n");

    for (indice = 0; indice < total_palabras_reservadas; indice++)
    {
        if (palabras_reservadas[indice].cantidad > 0)
        {
            printf(
                "%-15s %ld\n",
                palabras_reservadas[indice].lexema,
                palabras_reservadas[indice].cantidad
            );

            hay_resultados = 1;
        }
    }

    if (!hay_resultados)
    {
        printf("No se encontraron palabras reservadas.\n");
    }
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
"case"      { registrar_palabra_reservada("PR_CASE", yytext); }
"class"     { registrar_palabra_reservada("PR_CLASS", yytext); }
"data"      { registrar_palabra_reservada("PR_DATA", yytext); }
"default"   { registrar_palabra_reservada("PR_DEFAULT", yytext); }
"deriving"  { registrar_palabra_reservada("PR_DERIVING", yytext); }
"do"        { registrar_palabra_reservada("PR_DO", yytext); }
"else"      { registrar_palabra_reservada("PR_ELSE", yytext); }
"foreign"   { registrar_palabra_reservada("PR_FOREIGN", yytext); }
"if"        { registrar_palabra_reservada("PR_IF", yytext); }
"import"    { registrar_palabra_reservada("PR_IMPORT", yytext); }
"in"        { registrar_palabra_reservada("PR_IN", yytext); }
"infix"     { registrar_palabra_reservada("PR_INFIX", yytext); }
"infixl"    { registrar_palabra_reservada("PR_INFIXL", yytext); }
"infixr"    { registrar_palabra_reservada("PR_INFIXR", yytext); }
"instance"  { registrar_palabra_reservada("PR_INSTANCE", yytext); }
"let"       { registrar_palabra_reservada("PR_LET", yytext); }
"module"    { registrar_palabra_reservada("PR_MODULE", yytext); }
"newtype"   { registrar_palabra_reservada("PR_NEWTYPE", yytext); }
"of"        { registrar_palabra_reservada("PR_OF", yytext); }
"then"      { registrar_palabra_reservada("PR_THEN", yytext); }
"type"      { registrar_palabra_reservada("PR_TYPE", yytext); }
"where"     { registrar_palabra_reservada("PR_WHERE", yytext); }
"_"         { registrar_palabra_reservada("PR_COMODIN", yytext); }

    /* Palabras especiales usadas en importaciones. */
"as"        { registrar_palabra_reservada("KW_AS", yytext); }
"qualified" { registrar_palabra_reservada("KW_QUALIFIED", yytext); }
"hiding"    { registrar_palabra_reservada("KW_HIDING", yytext); }

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
registrar_identificador(yytext);
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
mostrar_frecuencia_palabras();

    fclose(archivo);

    return 0;
}