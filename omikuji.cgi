#!/usr/local/bin/perl
#+------------------------------------------------------------------------
#|���݂��� 1.0                                                  1999/06/26
#|                                (C)�s�v�c�G�̋�(http://yugen.main.jp/)
#+------------------------------------------------------------------------
###�Ăяo����������y�[�W
###http://����܂߂�URL�łȂ��Ə�肭�s���܂���B
$accept = 'http://your_domain/~your_account/cgi-bin/omikuji.html';



#�����������烆�[�U�ύX�s����
#+------------------------------------------------------------------------
if ($ENV{"HTTP_REFERER"} ne $accept) {		#���̃y�[�W����̌Ăяo���ɂ͉������Ȃ�
	exit;
} else {
	&rnd;
	&put_img;
	exit;
}

### [��������]
sub rnd {
	srand(time + $$);				#���������̏���
	$n = int(rand(6));				#�����𔭐�������
}

### [�C���[�W��\��]
sub put_img {
	open(IMG, "./${n}.gif");
	@data_gif = stat(IMG);
	$byte = $data_gif[7];					#�t�@�C���T�C�Y���擾
	print "Content-type: image/gif\n";		#HTTP�w�b�_��Ԃ�
	print "Content-length: $byte\n\n";		#�摜�T�C�Y���u���E�U�ɓn��
	print <IMG>;							#�o�C�i���f�[�^��n��
	close(IMG);
}
