from mrjob.job import MRJob

class EscrutinioNacional(MRJob):

    def mapper(self, _, linea):
        voto = linea.strip()
        # INICIA TU CODIGO AQUI
        if voto:
            yield voto, 1
        # TERMINA TU CODIGO AQUI

    def reducer(self, candidato, conteos):
        # INICIA TU CODIGO AQUI
        total = sum(conteos)
        yield candidato, total
        # TERMINA TU CODIGO AQUI

if __name__ == '__main__':
    EscrutinioNacional.run()
