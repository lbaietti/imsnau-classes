import { useState, useEffect } from "react";
import { Text, TextInput, Button, FlatList } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";

export default function App() {
    const [tarefas, setTarefas] = useState([]);
    const [nova, setNova] = useState('');

    const guardar = async () => {
        await AsyncStorage.setItem('tarefas', JSON.stringify(trefas));
    };

    const carregar = async () => {
        const dados = await AsyncStorage.getItem('tarefas');
        if(dados) setTarefas(JSON.parse(dados));
    };

    useEffect(() => { carregar(); }, []);
    useEffect(() => { guardar(); }, [tarefas]);
    return(
        <>
            <TextInput value={nova} onChangeText={setNova}/>
            <Button title="Adicionar" onPress={() => setTarefas([...tarefas, nova])}/>
            <FlatList data={tarefas} renderItem={({ item }) => <Text>{item}</Text>}/>
        </>
    );
}