<template>
  <h1>Criar Fazenda</h1>
  <router-link to="/"
    ><button type="button" class="btn btn-info">
      Voltar para Home
    </button></router-link
  >

  <form class="mx-1 mx-md-4">
    <div class="d-flex flex-row align-items-center mb-2">
      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
      <div class="form-outline flex-fill mb-0">
        <input type="text" id="form3Example1c" class="form-control" />
        <label class="form-label" for="form3Example1c">Nome da Fazenda</label>
      </div>
    </div>

    <div class="d-flex flex-row align-items-center mb-2">
      <i class="fas fa-envelope fa-lg me-3 fa-fw"></i>
      <div class="form-outline flex-fill mb-0">
        <input type="text" id="form3Example3c" class="form-control" />
        <label class="form-label" for="form3Example3c">Área</label>
      </div>
    </div>

    <div class="d-flex flex-row align-items-center mb-2">
      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
      <div class="form-outline flex-fill mb-0">
        <input type="text" id="form3Example4c" class="form-control" />
        <label class="form-label" for="form3Example4c">Centro_ID</label>
      </div>
    </div>

    <div class="d-flex flex-row align-items-center mb-2">
      <i class="fas fa-key fa-lg me-3 fa-fw"></i>
      <div class="form-outline flex-fill mb-0">
        <input type="text" id="form3Example4cd" class="form-control" />
        <label class="form-label" for="form3Example4cd">Geometria</label>
      </div>
    </div>

    <div class="d-flex flex-row align-items-center mb-2">
      <i class="fas fa-key fa-lg me-3 fa-fw"></i>
      <div class="form-outline flex-fill mb-0">
        <input type="text" id="form3Example4cd" class="form-control" />
        <label class="form-label" for="form3Example4cd">ID Dono</label>
      </div>
    </div>

    <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
      <button type="button" class="btn btn-primary btn-lg">Criar</button>
    </div>
  </form>
</template>

<script>
export default {
  name: "CriarForm",
};
</script>
