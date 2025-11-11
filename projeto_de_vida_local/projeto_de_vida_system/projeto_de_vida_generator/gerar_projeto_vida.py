# -*- coding: utf-8 -*-
"""
Sistema de Geração de Projeto de Vida Personalizado
Gera HTML personalizado para cada aluno com template MyResume
"""

import os
import re
import unicodedata
from pathlib import Path
import pandas as pd


class ProjetoVidaHTMLGenerator:
    """Gera HTML personalizado do Projeto de Vida para cada aluno"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.template_path = self.base_path / "MyResume" / "index.html"
        self.output_path = self.base_path / "htmls_gerados"
        self.images_path = self.base_path / "imagens_alunos"
        self.output_path.mkdir(exist_ok=True)
        
        # Carregar textos do modelo
        self.textos_modelo = self._load_textos_modelo()
        
    def _load_textos_modelo(self):
        """Carrega os textos do documento modelo"""
        modelo_path = self.base_path.parent / "documentos_modelo" / "Projeto de Vida - P Apresentação - v.10.pdf.txt"
        
        # Textos padrão caso o arquivo não exista
        textos = {
            "o_que_e_pfc": "Criado em 2009 pela UFSCar, o Programa Futuro Cientista® (PFC) é uma tecnologia social reconhecida e certificada que promove inclusão, desenvolvimento sustentável e acesso à universidade para jovens talentos em situação de vulnerabilidade.",
            "nota_presidente": "Este livreto é mais do que um material de leitura — é um sopro de esperança, é um verdadeiro Projeto de Vida.",
            "saudacao": "Olá, querido estudante!",
            "assinatura": "Prof. Dr. Fábio de Lima Leite\nUniversidade Federal de São Carlos\nPresidente do Programa Futuro Cientista®"
        }
        
        return textos
    
    def _normalizar_nome(self, nome):
        """Converte nome para formato de arquivo (sem acentos, com underline)"""
        # Remover acentos
        nome_norm = unicodedata.normalize('NFD', nome)
        nome_sem_acento = ''.join(char for char in nome_norm if unicodedata.category(char) != 'Mn')
        
        # Substituir espaços por underline
        nome_arquivo = nome_sem_acento.replace(' ', '_')
        
        # Remover caracteres especiais
        nome_arquivo = re.sub(r'[^\w_]', '', nome_arquivo)
        
        return nome_arquivo
    
    def _check_image_exists(self, nome_aluno, tipo='perfil'):
        """Verifica se existe imagem para o aluno"""
        nome_arquivo = self._normalizar_nome(nome_aluno)
        
        if tipo == 'perfil':
            for ext in ['.jpg', '.png', '.jpeg']:
                img_path = self.images_path / "fotos_perfil" / f"{nome_arquivo}{ext}"
                if img_path.exists():
                    # Retornar caminho relativo correto do HTML gerado
                    return f"../imagens_alunos/fotos_perfil/{nome_arquivo}{ext}"
        
        elif tipo == 'background':
            for ext in ['.jpg', '.png', '.jpeg']:
                img_path = self.images_path / "fotos_background" / f"{nome_arquivo}_bg{ext}"
                if img_path.exists():
                    # Retornar caminho relativo correto do HTML gerado
                    return f"../imagens_alunos/fotos_background/{nome_arquivo}_bg{ext}"
        
        # Retornar imagem padrão do template (já será ajustado com o prefixo ../MyResume/)
        if tipo == 'perfil':
            return "assets/img/profile-img.jpg"
        else:
            return "assets/img/hero-bg.jpg"
    
    def _check_logo_exists(self, universidade):
        """Verifica se existe logo para a universidade"""
        if pd.isna(universidade) or not universidade:
            return None
        
        # Normalizar nome da universidade para MAIÚSCULAS
        univ_upper = str(universidade).upper().strip()
        
        for ext in ['.png', '.jpg', '.jpeg']:
            logo_path = self.images_path / "logos_universidades" / f"{univ_upper}{ext}"
            if logo_path.exists():
                # Retornar caminho relativo correto do HTML gerado
                return f"../imagens_alunos/logos_universidades/{univ_upper}{ext}"
        
        return None
    
    def gerar_html_aluno(self, aluno_data):
        """
        Gera HTML personalizado para um aluno
        
        Args:
            aluno_data: Dict ou Series com dados do aluno
            
        Returns:
            Caminho do HTML gerado
        """
        # Converter para dict se for Series
        if isinstance(aluno_data, pd.Series):
            aluno_data = aluno_data.to_dict()
        
        nome_aluno = aluno_data.get('Seu Nome completo', 'Aluno')
        nome_arquivo = self._normalizar_nome(nome_aluno)
        
        print(f"   📄 Gerando HTML: {nome_aluno}")
        
        # Carregar template
        with open(self.template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()
        
        # Obter dados do aluno
        idade = aluno_data.get('Sua idade') or aluno_data.get('Idade atual') or aluno_data.get('Sua data de nascimento    ') or '---'
        escola = aluno_data.get('Escola', 'Escola')
        cidade = aluno_data.get('Cidade', 'Cidade')
        serie = aluno_data.get('Sua série na escola    ') or aluno_data.get('Sua série na escola ') or aluno_data.get('Sua série na escola') or '---'
        
        # Prioridades/Profissões
        prioridade_a = aluno_data.get('Sua Prioridade A', '')
        prioridade_b = aluno_data.get('Sua Prioridade B', '')
        
        # Converter para string e limpar valores NaN
        if pd.isna(prioridade_a):
            prioridade_a = ''
        else:
            prioridade_a = str(prioridade_a)
            
        if pd.isna(prioridade_b):
            prioridade_b = ''
        else:
            prioridade_b = str(prioridade_b)
        
        # Verificar imagens
        img_perfil = self._check_image_exists(nome_aluno, 'perfil')
        img_background = self._check_image_exists(nome_aluno, 'background')
        
        # Substituir dados no template
        html_personalizado = html_template
        
        # Corrigir caminhos dos assets (apontar para pasta MyResume)
        html_personalizado = html_personalizado.replace('href="assets/', 'href="../MyResume/assets/')
        html_personalizado = html_personalizado.replace('src="assets/', 'src="../MyResume/assets/')
        
        # Adicionar botão de voltar ao relatório
        btn_voltar = '''
    <!-- Botão Voltar ao Relatório -->
    <button id="btnVoltar"
       style="position: fixed; top: 20px; right: 20px; z-index: 9999; 
              background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); 
              color: white; padding: 12px 25px; border-radius: 25px; border: none;
              cursor: pointer; font-weight: 600; font-size: 0.95rem; 
              box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3); 
              transition: all 0.3s ease; display: flex; align-items: center; gap: 8px;"
       onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(231, 76, 60, 0.4)';"
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(231, 76, 60, 0.3)';"
       onclick="window.close(); if (!window.closed) { window.history.back(); }">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
        </svg>
        Voltar ao Relatório
    </button>
'''
        
        # Inserir botão após o <body>
        html_personalizado = html_personalizado.replace('<body class="index-page">', '<body class="index-page">\n' + btn_voltar)
        
        # Substituir nome
        html_personalizado = html_personalizado.replace('Brandon Johnson', nome_aluno)
        
        # Substituir profissões na digitação animada
        profissoes = []
        if prioridade_a.strip():
            profissoes.append(prioridade_a.strip())
        if prioridade_b.strip():
            profissoes.append(prioridade_b.strip())
        if not profissoes:
            profissoes = ["Futuro Cientista", "Estudante"]
        
        profissoes_str = ', '.join([f'"{p}"' for p in profissoes])
        html_personalizado = re.sub(
            r'data-typed-items="[^"]*"',
            f'data-typed-items="{", ".join(profissoes)}"',
            html_personalizado
        )
        
        # Substituir imagem de perfil
        # Se for caminho do template (assets/...), já foi ajustado para ../MyResume/assets/...
        # Se for imagem personalizada, já vem com caminho correto ../imagens_alunos/...
        if img_perfil.startswith('assets/'):
            img_perfil = '../MyResume/' + img_perfil
        html_personalizado = html_personalizado.replace('../MyResume/assets/img/profile-img.jpg', img_perfil)
        
        # Substituir imagem de background
        if img_background.startswith('assets/'):
            img_background = '../MyResume/' + img_background
        html_personalizado = html_personalizado.replace('../MyResume/assets/img/hero-bg.jpg', img_background)
        
        # Substituir informações pessoais
        html_personalizado = re.sub(
            r'UI/UX Designer &amp; Web Developer\.',
            f'Estudante do {serie} - {escola}',
            html_personalizado
        )
        
        # Adicionar seção de universidades
        universidades_html = self._gerar_secao_universidades(aluno_data)
        
        # Inserir universidades no lugar da seção de portfolio
        html_personalizado = re.sub(
            r'<!-- Portfolio Section -->.*?<!-- /Portfolio Section -->',
            universidades_html,
            html_personalizado,
            flags=re.DOTALL
        )
        
        # Adicionar informações sobre o PFC
        pfc_html = self._gerar_secao_pfc()
        
        # Inserir PFC no lugar da seção About
        html_personalizado = re.sub(
            r'<!-- About Section -->.*?<!-- /About Section -->',
            pfc_html.format(
                nome=nome_aluno,
                idade=idade,
                escola=escola,
                cidade=cidade,
                serie=serie
            ),
            html_personalizado,
            flags=re.DOTALL
        )
        
        # Salvar HTML
        output_file = self.output_path / f"{nome_arquivo}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_personalizado)
        
        print(f"      ✅ HTML salvo: {output_file}")
        return str(output_file)
    
    def _gerar_secao_pfc(self):
        """Gera seção sobre o PFC"""
        return """
    <!-- About Section -->
    <section id="about" class="about section">
      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Sobre o Aluno</h2>
        <p>Informações pessoais e trajetória no Programa Futuro Cientista</p>
      </div>
      
      <div class="container" data-aos="fade-up" data-aos-delay="100">
        <div class="row gy-4 justify-content-center">
          <div class="col-lg-4">
            <img src="assets/img/profile-img.jpg" class="img-fluid" alt="">
          </div>
          <div class="col-lg-8 content">
            <h2>{nome}</h2>
            <p class="fst-italic py-3">
              Estudante do Programa Futuro Cientista, dedicado ao desenvolvimento acadêmico e profissional.
            </p>
            <div class="row">
              <div class="col-lg-6">
                <ul>
                  <li><i class="bi bi-chevron-right"></i> <strong>Idade:</strong> <span>{idade}</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>Escola:</strong> <span>{escola}</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>Série:</strong> <span>{serie}</span></li>
                </ul>
              </div>
              <div class="col-lg-6">
                <ul>
                  <li><i class="bi bi-chevron-right"></i> <strong>Cidade:</strong> <span>{cidade}</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>Programa:</strong> <span>Futuro Cientista</span></li>
                </ul>
              </div>
            </div>
            <p class="py-3">
              Este documento apresenta o Projeto de Vida desenvolvido pelo aluno, incluindo suas aspirações profissionais, universidades sugeridas e o planejamento para alcançar seus objetivos.
            </p>
          </div>
        </div>
      </div>
    </section>
    <!-- /About Section -->
"""
    
    def _gerar_secao_universidades(self, aluno_data):
        """Gera seção de universidades sugeridas"""
        universidades_html = """
    <!-- Portfolio Section -->
    <section id="portfolio" class="portfolio section">
      <div class="container section-title" data-aos="fade-up">
        <h2>Universidades Sugeridas</h2>
        <p>Instituições recomendadas para seu desenvolvimento acadêmico</p>
      </div>
      
      <div class="container">
        <div class="row gy-4">
"""
        
        # Processar até 4 universidades (A, B, C, D)
        for letra in ['A', 'B', 'C', 'D']:
            univ = aluno_data.get(f'Universidade{letra}')
            if pd.notna(univ) and univ:
                curso = aluno_data.get(f'CursoUniv{letra}', 'Curso')
                tipo = aluno_data.get(f'TipoUniv{letra}', 'PÚBLICA')
                campus = aluno_data.get(f'Campus{letra}', 'Campus')
                duracao = aluno_data.get(f'DuracaoAnosCurso{letra}', '4 anos')
                periodo = aluno_data.get(f'Periodo{letra}', 'INTEGRAL')
                vestibular = aluno_data.get(f'Vestibular{letra}', 'ENEM')
                
                logo_url = self._check_logo_exists(univ)
                logo_html = f'<img src="{logo_url}" alt="{univ}" style="width: 80px; height: 80px; object-fit: contain; margin-bottom: 15px;">' if logo_url else ''
                
                universidades_html += f"""
          <div class="col-lg-6 col-md-6 portfolio-item isotope-item filter-app">
            <div style="background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;">
              <div style="text-align: center;">
                {logo_html}
                <h4 style="color: #2c3e50; margin-bottom: 15px;">{univ}</h4>
              </div>
              <div style="text-align: left;">
                <p style="margin: 8px 0;"><strong>Curso:</strong> {curso}</p>
                <p style="margin: 8px 0;"><strong>Tipo:</strong> <span style="color: #27ae60;">{tipo}</span></p>
                <p style="margin: 8px 0;"><strong>Campus:</strong> {campus}</p>
                <p style="margin: 8px 0;"><strong>Duração:</strong> {duracao}</p>
                <p style="margin: 8px 0;"><strong>Período:</strong> {periodo}</p>
                <p style="margin: 8px 0;"><strong>Vestibular:</strong> {vestibular}</p>
              </div>
            </div>
          </div>
"""
        
        universidades_html += """
        </div>
      </div>
    </section>
    <!-- /Portfolio Section -->
"""
        return universidades_html
    
    def gerar_todos(self, df_alunos):
        """Gera HTML para todos os alunos"""
        print(f"📚 Gerando HTMLs para {len(df_alunos)} alunos...")
        
        htmls_gerados = []
        for idx, row in df_alunos.iterrows():
            try:
                html_path = self.gerar_html_aluno(row)
                htmls_gerados.append(html_path)
            except Exception as e:
                nome = row.get('Seu Nome completo', f'Aluno_{idx}')
                print(f"      ❌ Erro ao gerar HTML para {nome}: {e}")
        
        print(f"\n✅ {len(htmls_gerados)} HTMLs gerados com sucesso!")
        return htmls_gerados


def main():
    """Função para testar o gerador"""
    print("🎯 Sistema de Geração de Projeto de Vida - HTML Personalizado")
    print("=" * 70)
    
    # Dados de exemplo
    aluno_teste = {
        'Seu Nome completo': 'João da Silva',
        'Sua idade': 15,
        'Escola': 'E.M. Exemplo',
        'Cidade': 'São Carlos',
        'Sua série na escola': '9º Ano',
        'Sua Prioridade A': 'Engenharia',
        'Sua Prioridade B': 'Arquitetura',
        'UniversidadeA': 'USP',
        'CursoUnivA': 'Engenharia Civil',
        'TipoUnivA': 'PÚBLICA',
        'CampusA': 'São Paulo',
        'DuracaoAnosCursoA': '5 anos',
        'PeriodoA': 'INTEGRAL',
        'VestibularA': 'FUVEST/ENEM'
    }
    
    generator = ProjetoVidaHTMLGenerator()
    html_path = generator.gerar_html_aluno(aluno_teste)
    
    print(f"\n✅ HTML de teste gerado: {html_path}")


if __name__ == "__main__":
    main()

