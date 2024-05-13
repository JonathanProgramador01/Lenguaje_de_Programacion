//#include <iostream>
//#include <vector>
//
//
//void imprimir(const std::vector<int>& source) {
//
//	for (const auto& elemtos : source) {
//		std::cout << elemtos << " ";
//	}
//
//	std::cout << std::endl;
//}
//void sort_reverst(std::vector<int>& Data) {
//
//	for (size_t i = 0; i < Data.size() - 1; i++) {
//
//		for (size_t j = 0; j < Data.size() - 1 - i; j++) {
//			if (Data[j] < Data[j + 1]) {
//
//				size_t temp = Data[j];
//				Data[j] = Data[j + 1];
//				Data[j + 1] = temp;
//			}
//		}
//
//
//	}
//
//}
//
//
//int main() {
//
//	std::vector<int> Data{ 3,1,10,6,9 };
//	// Antes 
//	imprimir(Data);
//	sort_reverst(Data);
//	// Despues 
//	imprimir(Data);
//
//	return 0;
//}


//#include <iostream>
//#include <array>
//#include <algorithm>
//
//
//const int FILAS = 3;
//const int COLUMNAS = 3;
//const int TOTAL = 9;
//
//
//std::array<std::array<int, COLUMNAS>, FILAS> TRES_POR_TRES(const std::array<int,TOTAL> &Arr) {
//
//	std::array<std::array<int, COLUMNAS>, FILAS> TwoArray;
//
//	int k = 0;
//	for (int i = 0; i < FILAS; i++) {
//
//		for (int j = 0; j < COLUMNAS; j++) {
//
//			TwoArray[i][j] = Arr[k++];
//
//		}
//
//	}
//
//
//
//	return TwoArray;
//
//}
//
//void imprimir(const std::array<std::array<int, COLUMNAS>, FILAS>& arr) {
//
//
//	for (const auto &fila : arr) {
//		for (int  Columnas : fila) {
//			std::cout << Columnas << " ";
//		}
//
//		std::cout << "\n";
//	}
//
//
//
//}
//
//
//
//int main() {
//
//	std::array<int, TOTAL> Data = { 5,2,4,8,9,4,12,2,0 };
//	std::sort(Data.begin(), Data.end());
//
//	std::array<std::array<int, COLUMNAS>, FILAS> Nueva_Data = TRES_POR_TRES(Data);
//
//	imprimir(Nueva_Data);
//	
//
//
//	return 0;
//}

