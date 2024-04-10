
#include <iostream> 

enum TipoTriangulo {
    EQUILATERO,
    ISOSCELES,
    ESCALENO,
    NO_TRIANGULO
};

TipoTriangulo tipo_triangulo(int a, int b, int c) {

    if (a == b && b == c)
        return EQUILATERO; 
    else if (a == b || a == c || b == c)
        return ISOSCELES;  
    else
        return ESCALENO;  
}

bool es_posible(int a, int b, int c) {
    if ((a + b) > c && (a + c) > b && (b + c) > a) {
        return true;
    }
    return false;
}

int main() {
    int a, b, c;
    std::cout << "Ingrese las medidas de los lados del triángulo: ";
    std::cin >> a >> b >> c;

    if (es_posible(a, b, c)) {

        TipoTriangulo tipo = tipo_triangulo(a, b, c);
        std::cout << "Es posible formar un triángulo. ";
        switch (tipo) {
        case EQUILATERO:
            std::cout << "Es un triángulo equilátero." << std::endl;
            break;
        case ISOSCELES:
            std::cout << "Es un triángulo isósceles." << std::endl;
            break;
        case ESCALENO:
            std::cout << "Es un triángulo escaleno." << std::endl;
            break;
        case NO_TRIANGULO:
            std::cout << "Error: Al menos una de las medidas es cero o negativa." << std::endl;
            break;
        }
    }
    else {
        std::cout << "Lo siento, pero con las medidas dadas no es posible formar un triángulo." << std::endl;
    }

    return 0;
}
