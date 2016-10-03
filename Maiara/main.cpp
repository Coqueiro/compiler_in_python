//
//  main.c
//  TrabalhoCompiladores
//

#include <iostream>
#include <stdio.h>
#include "analisador_lexico.h"
#include "analisador_sintatico.hpp"

#define LOG_PARSER

extern FILE* program_file;
extern FILE* out;
extern bool hasError;

using namespace std;

int main(int argc, const char * argv[]) {
    if(argc < 2){
        program_file = fopen("programa","r");
    }
    else{
        program_file = fopen(argv[0],"r");
    }
    
    if(argc < 3){
        out = fopen("machine.s","w+");
    }
    else{
        out = fopen(argv[1],"w+");
    }
    
    if(program_file == NULL || out == NULL){
        cout << "The file(s) does not exist or could not be opened" << endl;
        exit(1);
    }
    
    parse();
    
    if(!hasError){
        cout << "SUCESSO! O seu programa foi compilado corretamente =]" << endl;
    }
    else{
        cout << "Erros ocorreram durante a compilação." << endl;
    }
}