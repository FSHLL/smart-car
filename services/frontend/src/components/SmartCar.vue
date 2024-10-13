<template>
  <a-spin :spinning="spinning">
    <a-select
      v-model:value="operators"
      :options="options"
      mode="tags"
      placeholder="Operadores"
      size="large"
      style="width: 100%"
    ></a-select>
    <a-divider></a-divider>
    <a-row>
      <a-col :span="12">
        <div v-for="(row, rowIndex) in smartCarStore.matrix" :key="rowIndex" class="row">
            <div
              v-for="(cell, colIndex) in row"
              :key="colIndex"
              class="cell"
              :style="{backgroundColor: getColorByRepresentation(cell) }"
            >
            </div>
        </div>
      </a-col>
      <a-col :span="12">
        <h2>{{ getNameByAlgorithm(smartCarStore.algorithm[0]) }}</h2>
        <a-button block type="primary" v-if="smartCarStore.matrixString" @click="evaluate">Evaluar</a-button>
        <tree v-if="smartCarStore.solution?.tree"></tree>
        <a-divider></a-divider>
        <a-alert v-if="!spinning && smartCarStore.solution.cycle" message="Ciclo detectado intenta con otros operadores"  type="error"></a-alert>
        <a-alert v-if="!spinning && smartCarStore.solution.steps?.length === 0" message="Sin solución intenta con otros operadores" type="warning"></a-alert>
        <a-divider></a-divider>
        <a-descriptions v-if="smartCarStore.solution" title="Resultados">
          <a-row>
            <a-col :span="getSpan">
              <a-statistic title="Nodos expandidos" :value="smartCarStore.solution.expandedNodes" style="margin-right: 50px" />
            </a-col>
            <a-col :span="getSpan">
              <a-statistic title="Profundidad del arbol" :value="smartCarStore.solution.depth" style="margin-right: 50px" />
            </a-col>
            <a-col :span="getSpan">
              <a-statistic suffix="seg" title="Tiempo de computo" :value="smartCarStore.solution.time" :precision="2" style="margin-right: 50px" />
            </a-col>
            <a-col v-if="smartCarStore.solution?.cost" :span="getSpan">
              <a-statistic title="Costo" :value="smartCarStore.solution.cost" style="margin-right: 50px" />
            </a-col>
          </a-row>
        </a-descriptions>
      </a-col>
    </a-row>
  </a-spin>
</template>

<script setup>
import { getNameByAlgorithm } from '@/constants/algorithms';
import { getAllOperators } from '@/constants/operators';
import { getColorByRepresentation, representations } from '@/constants/representations';
import { useSmartCarStore } from '@/stores/smartCarStore';
import { message } from 'ant-design-vue';
import Tree from './Tree.vue';
import axios from 'axios';
import { computed, ref } from 'vue';

const spinning = ref(false);
const operators = ref(getAllOperators())

const options = getAllOperators().map(op => ({value: op}))
const smartCarStore = useSmartCarStore()

const getSpan = computed(() => smartCarStore.solution?.cost ? 6 : 8)

const evaluate = async () => {
  try {
    if (operators.value.length !== options.length) {
      message.warning('Selecciona el orden de tus operadores')
      return
    }
    spinning.value = true
    const response = await axios.post(`/${smartCarStore.algorithm[0]}`, {
      matrix: smartCarStore.matrixString,
      operators: operators.value
    })

    smartCarStore.solution = response.data
    printSolution()
  } catch (error) {
    message.error(error.message);
  } finally {
    spinning.value = false
  }
}

const printSolution = () => {
  smartCarStore.solution.steps.forEach((node, index) => {
    setTimeout(() => {
      const currentRepresentation = smartCarStore.matrix[node.row][node.col]
      smartCarStore.matrix[node.row][node.col] = representations.vehicle
      setTimeout(() => {
        if (index+1 !== smartCarStore.solution.steps.length) {
          smartCarStore.matrix[node.row][node.col] = currentRepresentation
        }
      }, 100 * index);
    }, 500 * index);
  });
}

</script>

<style>
.matrix {
  display: flex;
  flex-direction: column;
}
.row {
  display: flex;
}
.cell {
  width: 30px;
  height: 30px;
  border: 1px solid #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>