<template>
    <div>
        <a-button block @click="showModal">Diagrama</a-button>
        <a-modal v-model:open="open" width="1325px" title="Basic Modal">
            <ejs-diagram id="diagram" :width="width" :height="height" :layout="layout"
                :dataSourceSettings="dataSourceSettings" :getNodeDefaults="getNodeDefaults"
                :getConnectorDefaults="getConnectorDefaults">
            </ejs-diagram>
        </a-modal>
    </div>
</template>

<script setup>
import { DiagramComponent as EjsDiagram, DataBinding, HierarchicalTree, } from "@syncfusion/ej2-vue-diagrams";
import { provide, ref, watch } from "vue";
import { DataManager } from "@syncfusion/ej2-data";
import { useSmartCarStore } from "@/stores/smartCarStore";

const smartCarStore = useSmartCarStore()

const width = "1300px";
const height = "800px";

const open = ref(false);
const showModal = () => {
    open.value = true;
};

const getNodeDefaults = (node) => {
    node.height = 60;
    node.width = 150;
    return node;
};

const getConnectorDefaults = (obj) => {
    obj.type = "Orthogonal";
    obj.style = {
        strokeColor: "#6BA5D7",
        fill: "#6BA5D7",
        strokeWidth: 2,
    };
    obj.targetDecorator = {
        style: {
            fill: "#6BA5D7",
            strokeColor: "#6BA5D7",
        },
    };
    return obj;
};
const layout = {
    type: "OrganizationalChart",
};

const dataSourceSettings = ref({
    id: "id",
    parentId: "parent",
    dataManager: new DataManager(smartCarStore.solution?.tree),
    doBinding: (nodeModel, localData) => {
        nodeModel.annotations = [
            {
                content: `(${localData.position.row},${localData.position.col}) - C: ${localData.cost}`,
            }
        ];
        nodeModel.style = { fill: "#6BA5D7", strokeWidth: 0 };
    },
});

watch(
    () => smartCarStore.solution,
    (newSolution) => {
        dataSourceSettings.value.dataManager = new DataManager(newSolution.tree);
    },
    { immediate: true }
);

const diagram = [DataBinding, HierarchicalTree];
provide('diagram', diagram);
</script>

<style>
@import "@syncfusion/ej2-base/styles/material.css";
@import "@syncfusion/ej2-navigations/styles/material.css";
@import "@syncfusion/ej2-buttons/styles/material.css";
@import "@syncfusion/ej2-inputs/styles/material.css";
@import "@syncfusion/ej2-popups/styles/material.css";
@import "@syncfusion/ej2-vue-diagrams/styles/material.css";
</style>