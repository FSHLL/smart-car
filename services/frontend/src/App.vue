<template>
  <a-layout has-sider>
    <a-layout-sider
      :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0, top: 0, bottom: 0 }"
    >
      <div class="logo">
        <a-upload
              name="file"
              :before-upload="beforeFileUpload"
              :showUploadList="false"
            >
            <a-button>
              <upload-outlined></upload-outlined>
              Upload World
            </a-button>
      </a-upload>
      </div>
      <a-menu v-model:selectedKeys="smartCarStore.algorithm" theme="dark" mode="inline">
        <a-sub-menu key="sub1">
          <template #title>
            <span>
              <user-outlined />
              <span>No Informada</span>
            </span>
          </template>
          <a-menu-item :key="0">Amplitud</a-menu-item>
          <a-menu-item :key="1">Costo uniforme</a-menu-item>
          <a-menu-item :key="2">Profundidad evitando cliclos</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub2">
          <template #title>
            <span>
              <team-outlined />
              <span>Informada</span>
            </span>
          </template>
          <a-menu-item :key="3">Avara</a-menu-item>
          <a-menu-item :key="4">A*</a-menu-item>
        </a-sub-menu>
      </a-menu>
    </a-layout-sider>
    <a-layout :style="{ marginLeft: '200px' }">
      <a-layout-header :style="{ background: '#fff' }" >
        <a-typography>
          <a-typography-title :level="2">Smart Car</a-typography-title>
        </a-typography>
      </a-layout-header>
      <a-layout-content :style="{ margin: '24px 16px 0', overflow: 'initial' }">
        <div :style="{ padding: '24px', background: '#fff', textAlign: 'center' }">
          <SmartCar/>
        </div>
      </a-layout-content>
      <a-layout-footer :style="{ textAlign: 'center' }">
        Ant Design ©2018 Created by Ant UED
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useSmartCarStore } from './stores/smartCarStore';
import SmartCar from './components/SmartCar.vue';
import {
  UserOutlined,
  TeamOutlined,
  UploadOutlined
} from '@ant-design/icons-vue';

const matrix = ref([]);
const smartCarStore = useSmartCarStore()

const beforeFileUpload = (file) => {
  const reader = new FileReader();

  reader.onload = (e) => {
    const content = e.target.result;
    setMatrixContent(content)
  };

  if (file) {
    reader.readAsText(file);
  }

  return false;
};

const setMatrixContent = (content) => {
  matrix.value = content.split('\n').map(line => line.split(' ').map(Number));
  matrix.value.pop()
  smartCarStore.matrix = matrix.value
  smartCarStore.matrixString = content
}

watch(
    () => smartCarStore.algorithm,
    () => {
      smartCarStore.solution = {}
    },
    { immediate: true }
);
</script>


<style scoped>
.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
  text-align: center;
}
.site-layout .site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
  background: #141414;
}
</style>