#include <iostream>
#include <memory>
#include <vector>
#include <array>
#include <map>
#include <iomanip>

using namespace std;
const double PI = 3.1416;
int Limite = 50'000;





enum figuras
{
	RECTANGULO=1, TRIANGULO, CIRCULO
};
double rectangulo(double base,double altura) {

	if (base and altura >= 0)
		return base * altura;
	else
		return 0;

}
double triangulo(double base, double altura) {
	if (base and altura >= 0)
		return (base * altura) / 2;
	else
		return 0;
}
double ciruclo(double radio) { 

	if (radio >= 0)
		return PI * pow(radio, 2);
	else
		return 0;

}
void opciones() {
	std::cout << std::setw(70) <<setfill('=');
	std::cout << "\n\t\tEl granjero Pedro\n"
		<< std::setw(83)
		<< "\n1- Calcular area de un rectangulo" << std::endl
		<< "2- Calcular area de un triangulo" << std::endl
		<< "3- Calcular el area de un  circulo" << std::endl
		<<"0- Exit" << std::endl
		<<std::setw(68)
		<< "\nSelecciona (0-3): ";

}
void linea() {
	std::cout  << std::setw(50) << setfill('/')<<"\n";
}

void fertilizante(double Area) { // ten en cuenta que aqui estas agregando como la ara no tu base o tu altura o tu radio
	double ope = (Area * 50) / 1000; // 1000 METROS SON 50KG
	double gasto = ((ope / 50) * 950); // GASTO AREA /50 PARA SABER CUANTOS POR 950
	Limite -= gasto;
	if (Limite >= 0) {
		std::cout << "Requieres " << ope << "KG fertilizante :)" << std::endl;
		std::cout << "Gasto: " << gasto << " Tu limite ahora es de: " << Limite << std::endl;
	}
	else {
		Limite += gasto;
		std::cout << "Lo siento pero te has pasado de tu limite de 50,000" << std::endl;
	}

}


int main() {

	int opcion{};
	double base, altura,diametro,data;
	
	

	do {
		opciones();
		std::cin >> opcion;
		switch (opcion)
		{
		case RECTANGULO:
		{
			std::cout << "Ingresa Base y Altura: ";
			std::cin >> base>>altura;
			data = rectangulo(base, altura);
			linea();
			if (data != 0) {
				
				std::cout << "La area de tu rectangulo es de : " << data << std::endl;
			}
			else
				std::cout << "Error ingresa datos reales"<<std::endl;
			fertilizante(data);
			linea();
		}break;
		case TRIANGULO:
		{
			std::cout << "Ingresa Base y Altura: ";
			std::cin >> base >> altura;
			linea();
			data = triangulo(base, altura);
			if (data != 0) {
				std::cout << "La area de tu triangulo es de: " << data << std::endl;
			}
			else
				std::cout << "Error ingresa datos reales" << std::endl;
			fertilizante(data);
			linea();
		}break;
		case CIRCULO:
		{
			
			std::cout << "Ingresa el Diametro: ";
			std::cin >> diametro;
			data = ciruclo(diametro / 2);
			linea();
			if (data != 0) {
				std::cout << "La area de tu Circulo es de: " << data << std::endl;
			}
			else
				std::cout << "Error ingresa datos reales"<<std::endl;
			fertilizante(data);
			linea();
		}break;
		case 0:
			std::cout << "Fue un gusto atenderlo" << std::endl;
		default:
			std::cout << "Porfavor Selecciona Una opcion corecta :(" << std::endl;
			break;
		}
		
		std::cout << "\n\n\n";

	} while (opcion != 0);
	
		  
	return 0;
}
