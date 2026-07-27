const STATIC_URL = '/static/';

const dadosCurriculo = {
    perfil: {
        nome: "Meu Curriculo",
        subtitulo: "Estrutura Modular Oficial",
        tags: [
            { nome: "Minha História", icone: "💼" },
            { nome: "Programador", icone: "🖥️" },
            { nome: "SQL & Dados", icone: "🗄️" },
            { nome: "Automação", icone: "🤖" }
        ]
    },
    modulos: Array.from({length: 8}, (_, catIndex) => {
        const catNum = catIndex + 1;
        return {
            id: `categoria${catNum}`,
            imagem: `${STATIC_URL}categoria${catNum}.png`,
            subitens: Array.from({length: 8}, (_, subIndex) => {
                const subNum = subIndex + 1;
                return {
                    id: `c${catNum}_sub${subNum}`,
                    titulo: `Subitem ${subNum}`,
                    icone: '📌',
                    imagem: `${STATIC_URL}categoria${catNum}_sub${subNum}.png`,
                    texto: ''
                };
            })
        };
    })
};

let dados = JSON.parse(JSON.stringify(dadosCurriculo));
let subpageAtualId = null;

function carregarDados() {
    const salvo = localStorage.getItem('curriculo_modular_dados');
    if (salvo) {
        try {
            const parsed = JSON.parse(salvo);
            if (parsed && parsed.modulos) dados = parsed;
        } catch(e) {}
    }
}

function renderizarPerfil() {
    document.getElementById('profileName').textContent = dados.perfil.nome;
    document.getElementById('profileSubtitle').textContent = dados.perfil.subtitulo;
    const tagsDiv = document.getElementById('profileTags');
    tagsDiv.innerHTML = '';
    dados.perfil.tags.forEach(t => {
        tagsDiv.innerHTML += `<span class="tag">${t.icone} ${t.nome}</span>`;
    });
}

function renderizarModulos() {
    const grid = document.getElementById('modulesGrid');
    grid.innerHTML = '';
    dados.modulos.forEach(mod => {
        const card = document.createElement('div');
        card.className = 'module-card';
        card.style.backgroundImage = `url('${mod.imagem}')`;
        card.innerHTML = `<div class="click-hint">👆 Abrir Categoria</div>`;
        card.onclick = () => abrirModal(mod.id);
        grid.appendChild(card);
    });
}

function abrirModal(id) {
    const mod = dados.modulos.find(m => m.id === id);
    if (!mod) return;
    document.getElementById('modalTitle').textContent = `Módulo - ${id.toUpperCase()}`;
    const container = document.getElementById('subItemsContainer');
    container.innerHTML = '';
    mod.subitens.forEach(sub => {
        const btn = document.createElement('div');
        btn.className = 'sub-item-btn';
        btn.style.backgroundImage = `url('${sub.imagem}')`;
        btn.onclick = (e) => { e.stopPropagation(); abrirSubpage(sub.id); };
        container.appendChild(btn);
    });
    document.getElementById('modalOverlay').classList.add('aberto');
}

function fecharModal(e) {
    if (e && e.target !== e.currentTarget) return;
    document.getElementById('modalOverlay').classList.remove('aberto');
}

function abrirSubpage(subId) {
    subpageAtualId = subId;
    let subObj = null;
    for (const mod of dados.modulos) {
        const found = mod.subitens.find(s => s.id === subId);
        if (found) { subObj = found; break; }
    }
    if (!subObj) return;
    document.getElementById('subpageTitle').textContent = subObj.titulo;
    document.getElementById('subpageTextarea').value = subObj.texto || '';
    document.getElementById('subpageOverlay').classList.add('aberto');
}

function fecharSubpage(e) {
    if (e && e.target !== e.currentTarget) return;
    document.getElementById('subpageOverlay').classList.remove('aberto');
    subpageAtualId = null;
}

function salvarSubpageText() {
    if (!subpageAtualId) return;
    const texto = document.getElementById('subpageTextarea').value;
    for (const mod of dados.modulos) {
        for (const sub of mod.subitens) {
            if (sub.id === subpageAtualId) { sub.texto = texto; }
        }
    }
    salvarDadosLocal();
    fecharSubpage();
}

function salvarDadosLocal() {
    localStorage.setItem('curriculo_modular_dados', JSON.stringify(dados));
    mostrarToast('✅ Alterações salvas com sucesso!');
}

function resetarCache() {
    localStorage.removeItem('curriculo_modular_dados');
    location.reload();
}

function exportarDados() {
    salvarDadosLocal();
    const blob = new Blob([JSON.stringify(dados, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'curriculo_estruturado.json';
    a.click();
    URL.revokeObjectURL(url);
}

function mostrarToast(msg) {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.className = 'toast success show';
    setTimeout(() => toast.className = 'toast', 3000);
}

carregarDados();
renderizarPerfil();
renderizarModulos();