# Projeto-Pr-tico-de-Ciberseguran-a-Simula-o-de-Amea-as-e-Defesa
Laboratório prático de cibersegurança: simulação educacional de keylogger e ransomware em Python

# Projeto Prático de Cibersegurança: Simulação de Ameaças e Defesa 🛡️

Este repositório documenta um laboratório prático desenvolvido no contexto de estudos de cibersegurança. O objetivo principal é compreender, de maneira ética, controlada e em ambiente isolado, o funcionamento técnico de malwares comuns (Keylogger e Ransomware) para aprimorar o raciocínio analítico em estratégias de detecção, mitigação e resposta a incidentes.

> **⚠️ Aviso Legal:** Todo o código e material contido neste repositório possuem caráter estritamente educacional e acadêmico, executados em ambiente de laboratório controlado.

---

## 📂 Estrutura do Projeto

Os arquivos estão organizados da seguinte forma no repositório:

```text
/
├── ransomware/
│   ├── ransomware.py        # Script responsável por cifrar arquivos e gerar o resgate
│   ├── descriptografar.py   # Script de recuperação (restauração dos arquivos)
│   ├── chave.key            # Chave criptográfica gerada para o laboratório
│   └── LEIA ISSO.TXT        # Nota de resgate simulada
│
├── keylogger/
│   ├── keylogger0.pyw       # Versão inicial do keylogger (gravação local)
│   └── keylogger_email.pyw  # Versão avançada com envio automático por e-mail
│
└── README.md                # Documentação técnica do projeto
