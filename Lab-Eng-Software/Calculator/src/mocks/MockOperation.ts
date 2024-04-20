// src/mocks/MockOperation.ts
import { Operation } from "../interfaces/Operation";

class MockOperation implements Operation {
    somar(x: number, y: number): number {
        return x + y;
    }

    subtrair(x: number, y: number): number {
        return x - y;
    }

    multiplicar(x: number, y: number): number {
        return x * y;
    }

    dividir(x: number, y: number): number {
        if (y === 0) {
            throw new Error("Não é possível dividir por zero");
        }
        return x / y;
    }
}

export default MockOperation;
