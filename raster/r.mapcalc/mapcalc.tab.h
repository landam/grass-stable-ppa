/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_MAPCALC_TAB_H_INCLUDED
# define YY_YY_MAPCALC_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    VARNAME = 258,
    NAME = 259,
    VARSTRING = 260,
    STRING = 261,
    INTEGER = 262,
    FLOAT = 263,
    DOUBLE = 264,
    GT = 265,
    GE = 266,
    LT = 267,
    LE = 268,
    EQ = 269,
    NE = 270,
    LOGAND = 271,
    LOGOR = 272,
    LOGAND2 = 273,
    LOGOR2 = 274,
    BITAND = 275,
    BITOR = 276,
    LSH = 277,
    RSH = 278,
    RSHU = 279
  };
#endif
/* Tokens.  */
#define VARNAME 258
#define NAME 259
#define VARSTRING 260
#define STRING 261
#define INTEGER 262
#define FLOAT 263
#define DOUBLE 264
#define GT 265
#define GE 266
#define LT 267
#define LE 268
#define EQ 269
#define NE 270
#define LOGAND 271
#define LOGOR 272
#define LOGAND2 273
#define LOGOR2 274
#define BITAND 275
#define BITOR 276
#define LSH 277
#define RSH 278
#define RSHU 279

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 20 "mapcalc.y" /* yacc.c:1909  */

	int ival;
	double fval;
	char *sval;
	expression *exp;
	expr_list *list;

#line 110 "mapcalc.tab.h" /* yacc.c:1909  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_MAPCALC_TAB_H_INCLUDED  */
