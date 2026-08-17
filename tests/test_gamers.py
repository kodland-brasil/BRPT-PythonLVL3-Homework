import pytest
from gamers import Gamer


def test_Task_1_name_and_age_check():
    gamer = Gamer("João", 14, "JoaoForever", "joao@gmail.com")
    assert hasattr(gamer, 'name'), "A tarefa 1 não foi concluída. A classe 'Gamer' não contém o atributo 'name'"
    assert hasattr(gamer, 'age'), "A tarefa 1 não foi concluída. A classe 'Gamer' não contém o atributo 'age'"


def test_Task_2_add_nickname():
    gamer = Gamer("João", 14, "JoaoForever", "joao@gmail.com")
    assert hasattr(gamer, 'nickname'), "A tarefa 2 não foi concluída. A classe 'Gamer' não contém o atributo 'nickname'"


def test_Task_3_add_email():
    gamer = Gamer("João", 14, "JoaoForever", "joao@gmail.com")
    assert hasattr(gamer, 'email'), "A tarefa 3 não foi concluída. A classe 'Gamer' não contém o atributo 'email'"


def test_Task_4_change_message(capsys):
    gamer = Gamer("João", 14, "JoaoForever", "joao@gmail.com")
    gamer.introduce()
    captured = capsys.readouterr()
    expected_output = "Olá, meu nome é João, eu tenho 14 anos. Você sempre pode entrar em contato enviando um e-mail para joao@gmail.com. Procure-me no jogo pelo apelido JoaoForever."
    assert expected_output in captured.out, f"A tarefa 4 não foi concluída. Mensagem esperada: {expected_output}, O que obtivemos: {captured.out}"


if __name__ == "__main__":
    pytest.main(["-v"])