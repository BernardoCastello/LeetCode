public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        List<int> lista = new List<int>(nums);
        int operacoes = 0;

        while (true) {
            if (lista.Count <= 1){
                return operacoes;
            }

            bool estaOrdenado = true;
            long menorSoma = long.MaxValue; 
            int minIdx = -1;

            for (int i = 0; i < lista.Count - 1; i++) {
                if (lista[i] > lista[i + 1]) {
                    estaOrdenado = false;
                }
                long somaAtual = (long)lista[i] + lista[i + 1];

                if (somaAtual < menorSoma) {
                    menorSoma = somaAtual;
                    minIdx = i;
                }
            }

            if (estaOrdenado) {
                return operacoes;
            }

            lista[minIdx] = (int)menorSoma;
            lista.RemoveAt(minIdx + 1);
            operacoes++;
        }
    }
}