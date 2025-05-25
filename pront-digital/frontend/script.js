document.addEventListener('DOMContentLoaded', () => {
    const navButtons = document.querySelectorAll('.app-nav button');
    const menuIcon = document.getElementById('menuIcon');
    const nav = document.getElementById('navegacao-prontuario');
    const sections = document.querySelectorAll('section');
    const nextButtons = document.querySelectorAll('.next-button');
    const editButton = document.getElementById('editar-prontuario');
    const microphoneButtons = document.querySelectorAll('.microphone-button');
    let recognition = null;
    let isRecording = false;
    let currentInputId = null; // Variável para rastrear o input ativo

    function mostrarTela(telaId) {
        sections.forEach(section => {
            section.classList.add('hidden');
        });
        document.getElementById(telaId).classList.remove('hidden');
        navButtons.forEach(button => {
            button.classList.remove('ativo');
            if (button.getAttribute('data-tela') === telaId) {
                button.classList.add('ativo');
            }
        });
    }

    navButtons.forEach(button => {
        button.addEventListener('click', function() {
            const telaId = this.getAttribute('data-tela');
            mostrarTela(telaId);
            if (window.innerWidth <= 320) {
                nav.classList.remove('open');
                menuIcon.classList.remove('open');
            }
        });
    });

    menuIcon.addEventListener('click', () => {
        nav.classList.toggle('open');
        menuIcon.classList.toggle('open');
    });

    mostrarTela('identificacao');

    window.salvarProntuario = async function() {
    // Coleta os dados do formulário
    const dados = {};
    const formulario = document.getElementById('formulario-prontuario');
    const elementos = formulario.querySelectorAll('input, select, textarea');
    let camposObrigatorios = ['nome', 'data-nascimento', 'cpf', 'queixa-principal'];
    let camposVazios = [];

    elementos.forEach(elemento => {
        if (elemento.id) {
            if (camposObrigatorios.includes(elemento.id)) {
                dados[elemento.id] = elemento.value;
                if (!elemento.value) {
                    camposVazios.push(elemento.id);
                }
            } else {
                // Só adiciona os outros campos se não estiverem vazios
                if (elemento.value) {
                    dados[elemento.id] = elemento.value;
                }
            }
        }
    });

    if (camposVazios.length > 0) {
        alert('Preencha todos os campos obrigatórios: ' + camposVazios.join(', '));
        return;
    }

    // Monta o JSON no formato esperado pelo backend
    const payload = {
        paciente: {
            nome_paciente: dados['nome'],
            sexo: dados['sexo'] || "",
            data_nascimento: dados['data-nascimento'],
            cpf: dados['cpf'],
            telefone: dados['telefone'] || "Não informado",
        },
        prontuario: {
            data_consulta: new Date().toISOString().split('T')[0],
            queixa_principal: dados['queixa-principal'],
            historia_doenca_atual: dados['historia-doenca-atual'] || "",
            historico_medico_pregressa: dados['historico-medico-pregressa'] || "",
            historico_familiar: dados['historico-familiar'] || "",
            medicamentos_em_uso: dados['medicamentos-em-uso'] || "",
            alergias: dados['alergias'] || "",
            pressao_arterial: dados['pressao-arterial'] || "",
            frequencia_cardiaca: dados['frequencia-cardiaca'] || "",
            temperatura: dados['temperatura'] || "",
            observacoes_exame_fisico: dados['observacoes-exame-fisico'] || "",
            hipoteses_diagnosticas: dados['hipoteses-diagnosticas'] || "",
            diagnostico_definitivo: dados['diagnostico-definitivo'] || "",
            prescricao: dados['prescricao'] || "",
            orientacoes: dados['orientacoes'] || ""
        }
    };
    // Envia para o backend
    try {
        const response = await fetch('http://localhost:8000/prontuario/registrar-auto', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error('Erro ao registrar prontuário');
        }

        const result = await response.json();
        document.getElementById('dados-salvos').textContent = JSON.stringify(result, null, 2);
        document.getElementById('visualizacao-prontuario').classList.remove('hidden');
    } catch (error) {
        alert('Erro ao salvar prontuário: ' + error.message);
    }
    };

    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        recognition = new (window.webkitSpeechRecognition || window.SpeechRecognition)();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'pt-BR'; // Define o idioma aqui, para não repetir

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            const inputField = document.getElementById(currentInputId);
            if (inputField) {
                inputField.value = transcript;
            }
            stopRecording(); // Não precisa passar o botão aqui, pois rastreamos o estado globalmente
        };

        recognition.onspeechend = function() {
            stopRecording();
        };

        recognition.onerror = function(event) {
            console.error('Erro de reconhecimento de fala:', event.error);
            stopRecording();
            alert('Ocorreu um erro no reconhecimento de fala. Por favor, tente novamente.');
        };
    } else {
        console.warn('A API Web Speech não é suportada neste navegador.');
        microphoneButtons.forEach(button => {
            button.disabled = true;
            button.title = 'Reconhecimento de fala não suportado';
        });
    }

    function startRecording(button) {
        if (recognition && !isRecording) {
            currentInputId = button.getAttribute('data-input');
            recognition.start();
            isRecording = true;
            button.classList.add('recording');
            microphoneButtons.forEach(btn => {
                if (btn !== button) {
                    btn.classList.remove('recording'); // Garante que apenas um botão esteja "gravando" visualmente
                }
            });
        }
    }

    function stopRecording() {
        if (recognition && isRecording) {
            recognition.stop();
            isRecording = false;
            microphoneButtons.forEach(btn => {
                btn.classList.remove('recording');
            });
            currentInputId = null; // Limpa o input ativo
        }
    }

    microphoneButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (!isRecording) {
                startRecording(this);
            } else if (this.classList.contains('recording')) {
                stopRecording();
            } else {
                stopRecording(); // Interrompe qualquer outra gravação antes de iniciar uma nova
                startRecording(this);
            }
        });
    });

    nextButtons.forEach(button => {
        button.addEventListener('click', function() {
            const nextTelaId = this.getAttribute('data-next');
            mostrarTela(nextTelaId);
        });
    });

    if (editButton) {
        editButton.addEventListener('click', () => {
            mostrarTela('identificacao'); // Volta para a primeira tela para edição
        });
    }

    const buscarProntuarioButton = document.getElementById('buscar-prontuario');
    const cpfRecuperacaoInput = document.getElementById('cpf-recuperacao');
    const dadosPacienteRecuperadosPre = document.getElementById('dados-paciente-recuperados');

    buscarProntuarioButton.addEventListener('click', async () => {
        const cpfParaBuscar = cpfRecuperacaoInput.value.trim();
        if (cpfParaBuscar) {
            try {
                // Busca paciente pelo CPF
                const pacienteResp = await fetch(`http://localhost:8000/paciente/cpf/${cpfParaBuscar}`);
                if (!pacienteResp.ok) {
                    dadosPacienteRecuperadosPre.textContent = 'Paciente não encontrado para este CPF.';
                    return;
                }
                const paciente = await pacienteResp.json();

                // Busca prontuários do paciente pelo ID
                const prontuariosResp = await fetch(`http://localhost:8000/paciente/${paciente.id}/prontuarios`);
                if (!prontuariosResp.ok) {
                    dadosPacienteRecuperadosPre.textContent = 'Nenhum prontuário encontrado para este paciente.';
                    return;
                }
                const prontuarios = await prontuariosResp.json();

                if (prontuarios.length === 0) {
                    dadosPacienteRecuperadosPre.textContent = 'Nenhum prontuário encontrado para este paciente.';
                } else {
                    dadosPacienteRecuperadosPre.textContent = JSON.stringify(prontuarios, null, 2);
                }
            } catch (error) {
                dadosPacienteRecuperadosPre.textContent = 'Erro ao buscar prontuário: ' + error.message;
            }
        } else {
            dadosPacienteRecuperadosPre.textContent = 'Por favor, digite um CPF para buscar.';
        }
    });
    
});