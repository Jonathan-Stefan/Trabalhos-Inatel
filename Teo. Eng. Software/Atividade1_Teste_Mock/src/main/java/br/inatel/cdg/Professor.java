package br.inatel.cdg;

import java.util.List;

public class Professor {
    private String nome;
    private String sala;
    private String horarioDeAtendimento;
    private String periodo;
    private List<String> predio;

    public Professor(String nome, String sala, String horarioDeAtendimento, String periodo, List<String> string) {
        this.nome = nome;
        this.sala = sala;
        this.horarioDeAtendimento = horarioDeAtendimento;
        this.periodo = periodo;
        this.predio = string;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSala() {
        return sala;
    }

    public void setSala(String sala) {
        this.sala = sala;
    }

    public String getHorarioDeAtendimento() {
        return horarioDeAtendimento;
    }

    public void setHorarioDeAtendimento(String horarioDeAtendimento) {
        this.horarioDeAtendimento = horarioDeAtendimento;
    }

    public String getPeriodo() {
        return periodo;
    }

    public void setPeriodo(String periodo) {
        this.periodo = periodo;
    }

    public List<String> getPredio() {
        return predio;
    }

    public void setPredio(List<String> predio) {
        this.predio = predio;
    }
    @Override
    public String toString() {
        return "Professor{" +
                "nome='" + nome + '\'' +
                ", sala='" + sala + '\'' +
                ", horarioDeAtendimento='" + horarioDeAtendimento + '\'' +
                ", periodo='" + periodo + '\'' +
                ", predio=" + predio +
                '}';
    }
}
