# 🎯 Sistema de Geração de Projeto de Vida - PFC

## Estrutura Completa e Organizada

Sistema para gerar documentos personalizados "Projeto de Vida" usando template HTML profissional.

---

## 📁 Estrutura de Diretórios

```
projeto_de_vida_generator/
│
├── 📂 MyResume/                          # Template HTML principal
│   ├── index.html                        # Página principal do template
│   ├── assets/                           # Recursos do template
│   │   ├── css/                          # Estilos CSS
│   │   ├── js/                           # Scripts JavaScript
│   │   ├── img/                          # Imagens padrão do template
│   │   └── vendor/                       # Bibliotecas (Bootstrap, etc)
│   └── forms/                            # Formulários (se houver)
│
├── 📂 imagens_alunos/                    # ⭐ PASTA PRINCIPAL DE IMAGENS
│   │
│   ├── 📂 fotos_perfil/                  # Fotos dos alunos
│   │   ├── COMO_USAR.txt                 # Instruções detalhadas
│   │   ├── Joao_da_Silva.jpg             # Exemplo de foto
│   │   ├── Maria_Santos.jpg
│   │   └── ...
│   │
│   ├── 📂 fotos_background/              # Imagens de fundo personalizadas
│   │   ├── COMO_USAR.txt                 # Instruções detalhadas
│   │   ├── Joao_da_Silva_bg.jpg          # Exemplo de background
│   │   ├── background_padrao.jpg         # Imagem padrão (opcional)
│   │   └── ...
│   │
│   └── 📂 logos_universidades/           # Logos das universidades
│       ├── COMO_USAR.txt                 # Instruções detalhadas
│       ├── USP.png                       # Exemplo de logo
│       ├── UNICAMP.png
│       ├── UFSCAR.png
│       ├── IFSP.png
│       └── ...
│
├── 📂 pdfs_gerados/                      # PDFs finais (criado automaticamente)
│   ├── Projeto_de_Vida_Joao_Silva.pdf
│   ├── Projeto_de_Vida_Maria_Santos.pdf
│   └── ...
│
├── 📂 htmls_gerados/                     # HTMLs personalizados (criado automaticamente)
│   ├── Joao_da_Silva.html
│   ├── Maria_Santos.html
│   └── ...
│
└── 📄 README_ESTRUTURA.md                # Este arquivo
```

---

## 🎯 Fluxo de Funcionamento

### 1️⃣ **Preparação das Imagens**

```
📸 Adicione imagens nas pastas correspondentes:
   
   imagens_alunos/
   ├── fotos_perfil/          → Fotos dos alunos
   ├── fotos_background/      → Fundos personalizados
   └── logos_universidades/   → Logos das universidades
```

### 2️⃣ **Sistema Processa os Dados**

```
🔄 Para cada aluno no CSV:
   
   1. Carrega dados do aluno
   2. Procura foto de perfil (nome_do_aluno.jpg)
   3. Procura background personalizado (nome_do_aluno_bg.jpg)
   4. Procura logos das universidades sugeridas
   5. Gera HTML personalizado com todas as informações
```

### 3️⃣ **Geração dos Documentos**

```
📄 Sistema gera:
   
   ✅ HTML personalizado (htmls_gerados/nome_do_aluno.html)
   ✅ PDF do documento (pdfs_gerados/Projeto_de_Vida_nome.pdf)
```

---

## 🖼️ Convenção de Nomes de Arquivos

### ⚠️ **MUITO IMPORTANTE!**

Todos os arquivos de imagem devem seguir estas regras:

#### 📸 **Fotos de Perfil:**
```
Formato: Nome_Completo_Do_Aluno.extensao

✅ CORRETO:
   - Joao_da_Silva.jpg
   - Maria_Santos_Oliveira.png
   - Pedro_Henrique_Costa.jpg

❌ ERRADO:
   - João da Silva.jpg      (tem acento e espaço)
   - joao.jpg               (sem sobrenome)
   - foto_joao.jpg          (formato errado)
```

#### 🖼️ **Backgrounds Personalizados:**
```
Formato: Nome_Completo_Do_Aluno_bg.extensao

✅ CORRETO:
   - Joao_da_Silva_bg.jpg
   - Maria_Santos_bg.png

❌ ERRADO:
   - fundo_joao.jpg         (formato errado)
   - Joao_bg.jpg            (falta sobrenome)
```

#### 🎓 **Logos de Universidades:**
```
Formato: SIGLA_UNIVERSIDADE.extensao (MAIÚSCULAS)

✅ CORRETO:
   - USP.png
   - UNICAMP.png
   - UFSCAR.png
   - IFSP.png

❌ ERRADO:
   - usp.png                (minúscula)
   - logo_usp.png           (prefixo extra)
   - universidade.png       (não específico)
```

---

## 🔧 Regras de Conversão de Nomes

### **Do CSV para Nome de Arquivo:**

| CSV (original) | Nome do Arquivo |
|----------------|-----------------|
| `João da Silva` | `Joao_da_Silva.jpg` |
| `María José dos Santos` | `Maria_Jose_dos_Santos.jpg` |
| `José Pedrô Õliveira` | `Jose_Pedro_Oliveira.jpg` |

### **Regras:**
1. ✅ Remover acentos: `á é í ó ú ã õ ç` → `a e i o u a o c`
2. ✅ Substituir espaços por underline: ` ` → `_`
3. ✅ Manter apenas letras, números e underline
4. ✅ Primeira letra de cada palavra maiúscula

---

## 📊 Especificações Técnicas das Imagens

### 📸 **Fotos de Perfil:**
- **Formato:** JPG ou PNG
- **Tamanho:** 500x500 pixels (quadrado)
- **Proporção:** 1:1
- **Peso máximo:** 2MB
- **Qualidade:** Alta resolução, fundo neutro

### 🖼️ **Backgrounds:**
- **Formato:** JPG ou PNG
- **Tamanho:** 1920x1080 pixels (Full HD)
- **Proporção:** 16:9
- **Peso máximo:** 5MB
- **Estilo:** Profissional, não muito detalhado

### 🎓 **Logos:**
- **Formato:** PNG (transparente) ou JPG
- **Tamanho:** 300x300 pixels
- **Proporção:** 1:1 ou original
- **Peso máximo:** 500KB
- **Qualidade:** Vetorial ou alta resolução

---

## 💡 Dicas e Boas Práticas

### ✅ **Organização:**
1. Mantenha backup de todas as imagens originais
2. Use nomes padronizados desde o início
3. Teste com 2-3 alunos antes de processar todos
4. Verifique a qualidade das imagens antes de adicionar

### ✅ **Qualidade das Fotos:**
1. Boa iluminação
2. Fundo neutro ou profissional
3. Rosto centralizado
4. Expressão amigável
5. Roupa adequada

### ✅ **Logos das Universidades:**
1. Use apenas logos oficiais
2. Baixe em alta resolução
3. Prefira PNG com fundo transparente
4. Mantenha proporções originais
5. Respeite as cores oficiais

---

## 🚀 Próximos Passos

### **Fase 1: Preparação**
1. ✅ Estrutura de pastas criada
2. ⬜ Adicionar fotos dos alunos
3. ⬜ Baixar logos das universidades
4. ⬜ (Opcional) Adicionar backgrounds personalizados

### **Fase 2: Desenvolvimento**
1. ⬜ Adaptar template HTML para dados dinâmicos
2. ⬜ Criar sistema de geração de HTML personalizado
3. ⬜ Implementar conversão HTML → PDF
4. ⬜ Integrar com sistema de relatórios existente

### **Fase 3: Integração**
1. ⬜ Adicionar botão "Ver Projeto de Vida" na tabela de alunos
2. ⬜ Link para HTML gerado ao clicar no botão
3. ⬜ Botão de "Gerar PDF" na página HTML
4. ⬜ Sistema de download dos PDFs

---

## 📝 Checklist de Verificação

Antes de gerar os documentos, verifique:

### **Imagens:**
- [ ] Fotos de perfil dos alunos adicionadas
- [ ] Nomes dos arquivos seguem convenção (sem acentos, com underline)
- [ ] Imagens têm boa qualidade e resolução
- [ ] Logos das universidades em PNG transparente
- [ ] Todos os arquivos estão nas pastas corretas

### **Dados:**
- [ ] CSV com dados dos alunos está atualizado
- [ ] Nomes dos alunos no CSV correspondem aos nomes dos arquivos
- [ ] Universidades listadas têm logos disponíveis
- [ ] Dados estão completos e validados

### **Sistema:**
- [ ] Template MyResume está funcionando
- [ ] Estrutura de pastas está correta
- [ ] Scripts de geração estão prontos
- [ ] Conversão HTML → PDF testada

---

## 🆘 Solução de Problemas

### **Problema: Imagem não aparece**
**Soluções:**
1. Verifique se o nome do arquivo está correto
2. Confirme que a extensão é .jpg ou .png
3. Verifique se o arquivo está na pasta correta
4. Teste se o arquivo não está corrompido

### **Problema: Nome com acento não funciona**
**Solução:**
- Remova TODOS os acentos do nome do arquivo
- Use apenas letras sem acentuação
- Exemplo: `João` → `Joao`

### **Problema: Logo não aparece**
**Soluções:**
1. Verifique se o nome está em MAIÚSCULAS
2. Confirme que é a sigla correta da universidade
3. Verifique se o arquivo está na pasta `logos_universidades/`

---

## 📞 Suporte

Para dúvidas ou problemas:

1. Consulte os arquivos `COMO_USAR.txt` em cada pasta
2. Verifique este README
3. Teste com exemplos antes de processar em massa
4. Mantenha sempre backups das imagens originais

---

## 🎓 Desenvolvido para o Programa Futuro Cientista® 2025

**Transformando vidas pela educação e ciência** 🔬

---

_Última atualização: 10/11/2025_

