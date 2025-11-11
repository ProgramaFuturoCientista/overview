# 🔧 SOLUÇÃO: ERR_FILE_NOT_FOUND

## ⚠️ Problema Identificado

**Erro**: `ERR_FILE_NOT_FOUND`  
**Causa**: Navegadores modernos bloqueiam navegação entre arquivos locais (protocolo `file://`) por motivos de segurança.

---

## ✅ SOLUÇÃO: Usar Servidor Local

### **Método 1: Python HTTP Server** (Recomendado)

1. **Abra PowerShell** na pasta repo:
```powershell
cd "D:\Programa Futuro Cientista\direcao_geral\executivo\relatorio_semanal\output\repo"
```

2. **Inicie o servidor**:
```powershell
python -m http.server 8000
```

3. **Abra no navegador**:
```
http://localhost:8000
```

4. **Pronto!** Agora todos os links funcionarão perfeitamente! ✨

---

### **Método 2: PHP (Se tiver PHP instalado)**

```powershell
cd "D:\Programa Futuro Cientista\direcao_geral\executivo\relatorio_semanal\output\repo"
php -S localhost:8000
```

Depois abra: `http://localhost:8000`

---

### **Método 3: Node.js (Se tiver Node instalado)**

```powershell
cd "D:\Programa Futuro Cientista\direcao_geral\executivo\relatorio_semanal\output\repo"
npx http-server -p 8000
```

Depois abra: `http://localhost:8000`

---

### **Método 4: Extensão do VS Code**

Se usa VS Code:
1. Instale a extensão **Live Server**
2. Botão direito no `index.html`
3. Selecione: "Open with Live Server"

---

## 💡 Por Que Isso Acontece?

Navegadores modernos (Chrome, Edge, Firefox) **bloqueiam navegação** entre arquivos locais (`file://`) para evitar que sites maliciosos acessem arquivos do seu computador.

**Comportamento:**
- ✅ Arquivo direto funciona (clique duplo)
- ❌ Links entre arquivos NÃO funcionam
- ✅ Com servidor local TUDO funciona

---

## 🚀 SERVIDOR INICIADO PARA VOCÊ!

**Acabei de iniciar um servidor HTTP na porta 8000.**

**Acesse agora:**
```
http://localhost:8000
```

**Para parar o servidor:**
- Pressione `Ctrl + C` no terminal/PowerShell

---

## 🎯 Testando com Servidor Local

1. ✅ Abra: `http://localhost:8000`
2. ✅ Você verá a landing page
3. ✅ Clique em qualquer card de módulo
4. ✅ DEVE FUNCIONAR agora!
5. ✅ Teste o menu hambúrguer
6. ✅ Teste voltar para Home

---

## 📝 Comandos Úteis

### **Iniciar servidor**:
```powershell
cd "D:\Programa Futuro Cientista\direcao_geral\executivo\relatorio_semanal\output\repo"
python -m http.server 8000
```

### **Parar servidor**:
```
Ctrl + C
```

### **Usar outra porta** (se 8000 estiver ocupada):
```powershell
python -m http.server 8080
```

### **Abrir automaticamente no navegador**:
```powershell
python -m http.server 8000 & Start-Process "http://localhost:8000"
```

---

## 🌐 No GitHub Pages Funciona Normalmente

**IMPORTANTE**: Esse problema SÓ acontece localmente!

Quando você subir para GitHub Pages:
- ✅ Todos os links funcionarão perfeitamente
- ✅ Não precisa de servidor local
- ✅ GitHub Pages serve os arquivos via HTTP(S)

**URL do GitHub será**: `https://usuario.github.io/repo/`

---

## 🔍 Alternativa: Configurar Navegador

### **Chrome/Edge - Permitir file:// (NÃO RECOMENDADO)**

Abrir Chrome com flag especial:
```powershell
"C:\Program Files\Google\Chrome\Application\chrome.exe" --allow-file-access-from-files "file:///D:/Programa Futuro Cientista/direcao_geral/executivo/relatorio_semanal/output/repo/index.html"
```

⚠️ **ATENÇÃO**: Isso reduz a segurança do navegador!

---

## ✅ RESUMO

**Problema**: ERR_FILE_NOT_FOUND ao clicar em links  
**Causa**: Navegador bloqueia file:// por segurança  
**Solução**: Usar servidor local (HTTP)  
**Comando**: `python -m http.server 8000`  
**URL**: `http://localhost:8000`  

**No GitHub Pages**: Funciona perfeitamente! ✨

---

## 🎊 SERVIDOR JÁ ESTÁ RODANDO!

**Acesse agora:**
```
http://localhost:8000
```

**E teste os links!** 🚀

---

**Para parar o servidor:**
Vá no terminal/PowerShell e pressione **Ctrl + C**

---

**Programa Futuro Cientista® - UFSCar**  
Sistema de Relatórios v1.2  
Novembro 2025

