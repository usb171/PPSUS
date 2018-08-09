
class ExameClass():

    def get_dic_exames(self, lista_exames):
        dic_exames = {}
        for exame in lista_exames:
            chave = str(exame.fk_coleta.tipoExame)
            if dic_exames.get(chave):
                dic_exames[chave]['quantidade'] += 1
                dic_exames[chave]['data_criacao'].append(exame.dataCriacao.strftime('%A %d de %B de %Y, %H:%M:%S'))
                dic_exames[chave]['id_exame'].append(exame.id)
            else:
                dic_exames[chave] = {'quantidade':1,'data_criacao':[exame.dataCriacao.strftime('%A %d de %B de %Y, %H:%M:%S')], 'id_exame': [exame.id]}

        #datas_exames = list(map(lambda x: x.dataCriacao.strftime('%A %d de %B de %Y, %H:%M:%S'), exames))
        return dic_exames

    def get_dic_coletas(self, lista_coletas):
        dic_coletas = {}
        for coleta in lista_coletas:
            # print(coleta, " ", coleta.tipoExame)
            chave = str(coleta.tipoExame)
            if dic_coletas.get(chave):
                dic_coletas[chave]['quantidade'] += 1
                dic_coletas[chave]['data_criacao'].append(coleta.dataCriacao.strftime('%A %d de %B de %Y, %H:%M:%S'))
                dic_coletas[chave]['id_exame'].append(coleta.id)
            else:
                dic_coletas[chave] = {'quantidade':1,'data_criacao':[coleta.dataCriacao.strftime('%A %d de %B de %Y, %H:%M:%S')], 'id_exame': [coleta.id]}

        #datas_exames = list(map(lambda x: x.dataCriacao.strftime('%A %d de %B de %Y, %H:%M:%S'), exames))
        return dic_coletas
