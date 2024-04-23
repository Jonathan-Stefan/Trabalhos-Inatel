import Calculator from "./Calculator";
import MockOperation from "./mocks/MockOperation";

describe("Calculator Tests", () => {
    let calculator: Calculator;

    beforeEach(() => {
        // Criando uma instância da Calculator com a classe mock MockOperation
        calculator = new Calculator(new MockOperation());
    });

    test("Addition test", () => {
        const result = calculator.somar(2, 3);
        expect(result).toBe(5);
    });

    test("Subtraction test", () => {
        const result = calculator.subtrair(5, 3);
        expect(result).toBe(2);
    });

    test("Multiplication test", () => {
        const result = calculator.multiplicar(5, 3);
        expect(result).toBe(15);
    });

    test("Division test", () => {
        const result = calculator.dividir(6, 3);
        expect(result).toBe(2);
    });

    test("Division by zero test", () => {
        expect(() => {
            calculator.dividir(6, 0);
        }).toThrowError("Não é possível dividir por zero");
    });
});