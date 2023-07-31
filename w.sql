
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (1, 'Cardiologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`,`nome`, `created_at`, `updated_at`, `deleted_at`) VALUES (2,'Exames', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (4, 'Pneumologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (5, 'Neurologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (7, 'Consultas', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (8, 'Retorno', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (9, 'Endoscopia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (10, 'Ginecologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (18, 'Fisioterapia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (19, 'Fonoaudiologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (23, 'Laboratório', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (24, 'Densitometria', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (25, 'Mamografia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (26, 'Ultrassonografia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (27, 'Raios-X', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (28, 'Urologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (29, 'Ortopedia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (30, 'Odontologia','2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (31, 'Tomografia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (32, 'Oftalmologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (33, 'Proctologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (34, 'Vascular', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (35, 'Otorrino','2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (36, 'Alergista','2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (37, 'Dermatologia', '2023-05-25 17:28:00', NULL, NULL);
INSERT INTO `categoria_servico` (`id`, `nome`, `created_at`, `updated_at`, `deleted_at`)VALUES (38, 'Psiquiatria', '2023-05-25 17:28:00', NULL, NULL);





INSERT INTO laudo (laudo.paciente_id, laudo.servico_id, laudo.conteudo, laudo.dtentrega, 
laudo.nome_realizante, laudo.crm_realizante, laudo.is_legado, laudo.entregue, laudo.laudo_estado_id,
laudo.created_at)
SELECT e.paciente_id, s.id, l.conteudo, e.data_entrega, e.nome_realizante,
e.crm_realizante, "T","T", 5,
DATE_FORMAT( e.data_realizacao, "%Y-%m-%d %T" ) AS data_realizacao
From laudos_legado l
JOIN exames_legado e
	ON  l.codigo = CONCAT("L",e.guia,"_",e.ordem) 
JOIN servico s
 	ON  s.codigo = e.mnemonico
;
