# -*- coding: utf-8 -*-
import scrapy


class MetrocuadradoSpider(scrapy.Spider):
    name = 'metroCuadrado'
    allowed_domains = ['metrocuadrado.com']
    start_urls = ['https://www.metrocuadrado.com/edificio-de-apartamentos-edificio-de-oficinas-fincas-lotes-locales-consultorios-bodegas-oficinas-apartamentos-casas']
    

    def parse(self, response):
        aptos = response.xpath('//div[@class="content"]')
        for apto in aptos:
            absolut_url = apto.xpath('.//div/a[@itemprop="url"]/@href').get()
            name = apto.xpath('.//div/a/h2/text()').get()
            next_page =response.xpath('//div[@class="pager"]/a[@class="next list"]/@href').get()
            yield scrapy.Request(url =absolut_url, callback = self.parse_apto,meta = {'apto_name':name, 'url':absolut_url,'next_page' : next_page})#voy a enviar cada response 
        
        next_page =response.xpath('//div[@class="pager"]/a[@class="next list"]/@href').get()
        #if next_page:
        #    yield scrapy.Request(url = next_page,callback=self.parse)

    def parse_apto(self,response):
        name = response.request.meta['apto_name']
        url = response.request.meta['url']
        next_page = response.request.meta['next_page']


            
        DatosGenerales = list()
        DatosGeneralesRespuesta = list()
        DatosPrincipales = list()
        DatosPrincipalesRespuesta = list()
        DatosInfo = list()
        DatosInfoRespuesta = list()
        DatosComplementos = list()
        DatosComplementosRespuesta = list()

        for i in range(1,12): #pongo uno mas por que empiezo desde uno para que coincida abajo (abajo esta en 26)
            DatosGenerales.append("")
            DatosGeneralesRespuesta.append("")

        for i in range(1,22): 
            DatosPrincipales.append("")
            DatosPrincipalesRespuesta.append("")


        for i in range(1,32): 
            DatosComplementos.append("")
            DatosComplementosRespuesta.append("")
            DatosInfo.append("")
            DatosInfoRespuesta.append("")


        #Datos General
        for i in range(1,11):
            PalabraBuscar = 'normalize-space((//div[@class="m_property_info_table"]/dl)[' +str(i)+ ']/dt/h3/text())'
            PalabraBuscarResultado = 'normalize-space((//div[@class="m_property_info_table"]/dl)[' +str(i)+ ']/dd/text())'
            #si no la encuentra esta con otro nombre
            if not response.xpath(PalabraBuscar).get():
                PalabraBuscar = 'normalize-space((//div[@class="m_property_info_table new"]/dl)[' +str(i)+ ']/dt/h3/text())'
                PalabraBuscarResultado = 'normalize-space((//div[@class="m_property_info_table new"]/dl)[' +str(i)+ ']/dd/text())'

            if response.xpath(PalabraBuscar).get(): #si no encuentro este tampoco me salgo
                DatosGenerales[i]= response.xpath(PalabraBuscar).get()
                DatosGeneralesRespuesta[i] = response.xpath(PalabraBuscarResultado).get()
            else: 
                break
        
        #Datos Principales
        for i in range(1,21):
            PalabraBuscar = 'normalize-space((//div[@class="m_property_info_details"]/dl/dt/h3)['+str(i)+']/text())'
            PalabraBuscarResultado = 'normalize-space((//div[@class="m_property_info_details"]/dl/dd/h4)['+str(i)+']/text())'
            if response.xpath(PalabraBuscar).get():
                DatosPrincipales[i]= response.xpath(PalabraBuscar).get()
                DatosPrincipalesRespuesta[i] = response.xpath(PalabraBuscarResultado).get()
            else: 
                break

        #Datos Info
        for i in range(1,31):
            PalabraBuscar = 'normalize-space((//div[@class="m_property_info_details more_info"]/dl/dt/h3)['+str(i)+']/text())'
            PalabraBuscarResultado = 'normalize-space((//div[@class="m_property_info_details more_info"]/dl/dd/h4)['+str(i)+']/text())'
            if response.xpath(PalabraBuscar).get():
                DatosInfo[i]= response.xpath(PalabraBuscar).get()
                DatosInfoRespuesta[i] = response.xpath(PalabraBuscarResultado).get()
            else: 
                break

        #Datos Complementos
        for i in range(1,31):
            PalabraBuscar = 'normalize-space((//div[@class="m_property_info_details services complements show"]/ul/li/h4)['+str(i)+']/text())'
            if not response.xpath(PalabraBuscar).get():
                PalabraBuscar ='normalize-space((//div[@class="m_property_info_details services"]/ul/li/h3)['+str(i)+']/text())'
            if not response.xpath(PalabraBuscar).get():
                PalabraBuscar = 'normalize-space((//div[@class="m_property_info_details services complements"]/ul/li/h4)['+str(i)+']/text())'

            if response.xpath(PalabraBuscar).get():
                DatosComplementos[i]= response.xpath(PalabraBuscar).get()
                DatosComplementosRespuesta[i] = "Si"
            else: 
                break

                
                

        yield{
            "Nombre" : name,
            DatosGenerales[1] : DatosGeneralesRespuesta[1],
            DatosGenerales[2] : DatosGeneralesRespuesta[2],
            DatosGenerales[3] : DatosGeneralesRespuesta[3],
            DatosGenerales[4] : DatosGeneralesRespuesta[4],
            DatosGenerales[5] : DatosGeneralesRespuesta[5],
            DatosGenerales[6] : DatosGeneralesRespuesta[6],
            DatosGenerales[7] : DatosGeneralesRespuesta[7],
            DatosGenerales[8] : DatosGeneralesRespuesta[8],
            DatosGenerales[9] : DatosGeneralesRespuesta[9],
            DatosGenerales[10] : DatosGeneralesRespuesta[10],

            DatosPrincipales[1] : DatosPrincipalesRespuesta[1],
            DatosPrincipales[2] : DatosPrincipalesRespuesta[2],
            DatosPrincipales[3] : DatosPrincipalesRespuesta[3],
            DatosPrincipales[4] : DatosPrincipalesRespuesta[4],
            DatosPrincipales[5] : DatosPrincipalesRespuesta[5],
            DatosPrincipales[6] : DatosPrincipalesRespuesta[6],
            DatosPrincipales[7] : DatosPrincipalesRespuesta[7],
            DatosPrincipales[8] : DatosPrincipalesRespuesta[8],
            DatosPrincipales[9] : DatosPrincipalesRespuesta[9],
            DatosPrincipales[10] : DatosPrincipalesRespuesta[10],
            DatosPrincipales[11] : DatosPrincipalesRespuesta[11],
            DatosPrincipales[12] : DatosPrincipalesRespuesta[12],
            DatosPrincipales[13] : DatosPrincipalesRespuesta[13],
            DatosPrincipales[14] : DatosPrincipalesRespuesta[14],
            DatosPrincipales[15] : DatosPrincipalesRespuesta[15],
            DatosPrincipales[16] : DatosPrincipalesRespuesta[16],
            DatosPrincipales[17] : DatosPrincipalesRespuesta[17],
            DatosPrincipales[18] : DatosPrincipalesRespuesta[18],
            DatosPrincipales[19] : DatosPrincipalesRespuesta[19],
            DatosPrincipales[20] : DatosPrincipalesRespuesta[20],

            DatosInfo[1] : DatosInfoRespuesta[1],
            DatosInfo[2] : DatosInfoRespuesta[2],
            DatosInfo[3] : DatosInfoRespuesta[3],
            DatosInfo[4] : DatosInfoRespuesta[4],
            DatosInfo[5] : DatosInfoRespuesta[5],
            DatosInfo[6] : DatosInfoRespuesta[6],
            DatosInfo[7] : DatosInfoRespuesta[7],
            DatosInfo[8] : DatosInfoRespuesta[8],
            DatosInfo[9] : DatosInfoRespuesta[9],
            DatosInfo[10] : DatosInfoRespuesta[10],
            DatosInfo[11] : DatosInfoRespuesta[11],
            DatosInfo[12] : DatosInfoRespuesta[12],
            DatosInfo[13] : DatosInfoRespuesta[13],
            DatosInfo[14] : DatosInfoRespuesta[14],
            DatosInfo[15] : DatosInfoRespuesta[15],
            DatosInfo[16] : DatosInfoRespuesta[16],
            DatosInfo[17] : DatosInfoRespuesta[17],
            DatosInfo[18] : DatosInfoRespuesta[18],
            DatosInfo[19] : DatosInfoRespuesta[19],
            DatosInfo[20] : DatosInfoRespuesta[20],
            DatosInfo[21] : DatosInfoRespuesta[21],
            DatosInfo[22] : DatosInfoRespuesta[22],
            DatosInfo[23] : DatosInfoRespuesta[23],
            DatosInfo[24] : DatosInfoRespuesta[24],
            DatosInfo[25] : DatosInfoRespuesta[25],
            DatosInfo[26] : DatosInfoRespuesta[26],
            DatosInfo[27] : DatosInfoRespuesta[27],
            DatosInfo[28] : DatosInfoRespuesta[28],
            DatosInfo[29] : DatosInfoRespuesta[29],
            DatosInfo[30] : DatosInfoRespuesta[30],

            DatosComplementos[1] : DatosComplementosRespuesta[1],
            DatosComplementos[2] : DatosComplementosRespuesta[2],
            DatosComplementos[3] : DatosComplementosRespuesta[3],
            DatosComplementos[4] : DatosComplementosRespuesta[4],
            DatosComplementos[5] : DatosComplementosRespuesta[5],
            DatosComplementos[6] : DatosComplementosRespuesta[6],
            DatosComplementos[7] : DatosComplementosRespuesta[7],
            DatosComplementos[8] : DatosComplementosRespuesta[8],
            DatosComplementos[9] : DatosComplementosRespuesta[9],
            DatosComplementos[10] : DatosComplementosRespuesta[10],
            DatosComplementos[11] : DatosComplementosRespuesta[11],
            DatosComplementos[12] : DatosComplementosRespuesta[12],
            DatosComplementos[13] : DatosComplementosRespuesta[13],
            DatosComplementos[14] : DatosComplementosRespuesta[14],
            DatosComplementos[15] : DatosComplementosRespuesta[15],
            DatosComplementos[16] : DatosComplementosRespuesta[16],
            DatosComplementos[17] : DatosComplementosRespuesta[17],
            DatosComplementos[18] : DatosComplementosRespuesta[18],
            DatosComplementos[19] : DatosComplementosRespuesta[19],
            DatosComplementos[20] : DatosComplementosRespuesta[20],
            DatosComplementos[21] : DatosComplementosRespuesta[21],
            DatosComplementos[22] : DatosComplementosRespuesta[22],
            DatosComplementos[23] : DatosComplementosRespuesta[23],
            DatosComplementos[24] : DatosComplementosRespuesta[24],
            DatosComplementos[25] : DatosComplementosRespuesta[25],
            DatosComplementos[26] : DatosComplementosRespuesta[26],
            DatosComplementos[27] : DatosComplementosRespuesta[27],
            DatosComplementos[28] : DatosComplementosRespuesta[28],
            DatosComplementos[29] : DatosComplementosRespuesta[29],
            DatosComplementos[30] : DatosComplementosRespuesta[30],
            'url' : url
            #'User-Agent': response.request.headers.get('User-Agent').decode('utf-8')
        }


