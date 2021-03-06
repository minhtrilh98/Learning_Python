# Make a program that translates mRNA into protein
# It should report the longest ORF in each mRNA
# Make sure you translate all 3 reading frames on both strands
# It should use argparse and your library, of course
import argparse
import mcb185
import sys
# setup
parser = argparse.ArgumentParser(description='Search ORF and translate ORF')
# required arguments

parser.add_argument('--fasta', required=False, type=str, default='fasta',
	metavar='<str>', help='optional string argument [%(default)s]')

arg = parser.parse_args()


gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

for name, seq in mcb185.read_fasta(arg.fasta):
    protein = ''
    for i in range (0,len(mcb185.longest_orf(seq)),3):
        codon = mcb185.longest_orf(seq)[i:i+3]
        if codon in gcode: protein += gcode[codon]
        else:              protein += 'X'
    print(name)
    print(protein)

"""
python3 translate_mRNA.py --fasta hs_rna.fa
>NM_001368885.1
MVAERTHKAAATGARGPGELGAPGTVALVAARAERGARLPSPGSCGLLTLALCSLALSLLAHFRTAELQARVLRLEAERG
EQQMETAILGRVNQLLDEKWKLHSRRRREAPKTSPGCNCPPGPPGPTGRPGLPGVKGQPGEKGSPGDAGLSIIGPRGPPG
QPGTRGFPGFPGPIGLDGKPGHPGPKGDMGLTGPPGQPGPQGQKGEKGQCGEYPHRLLPLLNSVRLAPPPVIKRRTFQGE
QSQASIQGPPGPPGPPGPSGPLGHPGLPGPMGPPGLPGPPGPKGDPGIQGYHGRKGERGMPGMPGKHGAKGAPGIAVAGM
KGEPGIPGTKGEKGAEGSPGLPGLLGQKGEKGDAGNSIGGGRGEPGPPGLPGPPGPKGEAGVDGQVGPPGQPGDKGERGA
AGEQGPDGPKGSKGEPGKGEMVDYNGNINEALQEIRTLALMGPPGLPGQIGPPGAPGIPGQKGEIGLPGPPGHDGEKGPR
GKPGDMGPPGPQGPPGKDGPPGVKGENGHPGSPGEKGEKGETGQAGSPGLQGVPGPKGEAGLDGAKGEKGFQGEKGDRGP
LGLPGTPGPIGVPGPAGPKGERGSKGDPGMTGPTGAAGLPGLHGPPGDKGNRGHRGFKGEKGEPGLPGLDGLDAPCPLGE
DGLPVQGCWNK
>NM_001368886.1
MGLTGPPGQPGPQGQKGEKGQCGEYPHRLLPLLNSVRLAPPPVIKRRTFQGEQSQASIQGPPGPPGPPGPSGPLGHPGLP
GPMGPPGLPGPPGPKGDPGIQGYHGRKGERGMPGMPGKHGAKGAPGIAVAGMKGEPGIPGTKGEKGAEGSPGLPGLLGQK
GEKGDAGNSIGGGRGEPGPPGLPGPPGPKGEAGVDGQVGPPGQPGDKGERGAAGEQGPDGPKGSKGEPGKGEMVDYNGNI
NEALQEIRTLALMGPPGLPGQIGPPGAPGIPGQKGEIGLPGPPGHDGEKGPRGKPGDMGPPGPQGPPGKDGPPGVKGENG
HPGSPGEKGEKGETGQAGSPVPGLPGPEGPPGPPGLQGVPGPKGEAGLDGAKGEKGFQGEKGDRGPLGLPGTPGPIGVPG
PAGPKGERGSKGDPGMTGPTGAAGLPGLHGPPGDKGNRGHRGFKGEKGEPGLPGLDGLDAPCPLGEDGLPVQGCWNK
>NR_148047.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NR_148053.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NM_001374457.1
MSTPDPPLGGTPRPGPSPGPGPSPGAMLGPSPGPSPGSAHSMMGPSPGPPSAGHPIPTQGPGGYPQDNMHQMHKPMESMH
EKGMSDDPRYNQMKGMGMRSGGHAGMGPPPSPMDQHSQGYPSPLGGSEHASSPVPASGPSSGPQMSSGPGGAPLDGADPQ
ALGQQNRGPTPFNQNQLHQLRAQIMAYKMLARGQPLPDHLQMAVQGKRPMPGMQQQMPTLPPPSVSATGPGPGPGPGPGP
GPGPAPPNYSRPHGMGGPNMPPPGPSGVPPGMPGQPPGGPPKPWPEGPMANAAAPTSTPQKLIPPQPTGRPSPAPPAVPP
AASPVMPPQTQSPGQPAQPAPMVPLHQKQSRITPIQKPRGLDPVEILQEREYRLQARIAHRIQELENLPGSLAGDLRTKA
TIELKALRLLNFQRQLRQEVVVCMRRDTALETALNAKAYKRSKRQSLREARITEKLEKQQKIEQERKRRQKHQEYLNSIL
QHAKDFKEYHRSVTGKIQKLTKAVATYHANTEREQKKENERIEKERMRRLMAEDEEGYRKLIDQKKDKRLAYLLQQTDEY
VANLTELVRQHKAAQVAKEKKKKKKKKKAENAEGQTPAIGPDGEPLDETSQMSDLPVKVIHVESGKILTGTDAPKAGQLE
AWLEMNPGYEVAPRSDSEESGSEEEEEEEEEEQPQAAQPPTLPVEEKKKIPDPDSDDVSEVDARHIIENAKQDVDDEYGV
SQALARGLQSYYAVAHAVTERVDKQSALMVNGVLKQYQIKGLEWLVSLYNNNLNGILADEMGLGKTIQTIALITYLMEHK
RINGPFLIIVPLSTLSNWAYEFDKWAPSVVKVSYKGSPAARRAFVPQLRSGKFNVLLTTYEYIIKDKHILAKIRWKYMIV
DEGHRMKNHHCKLTQVLNTHYVAPRRLLLTGTPLQNKLPELWALLNFLLPTIFKSCSTFEQWFNAPFAMTGEKVDLNEEE
TILIIRRLHKVLRPFLLRRLKKEVEAQLPEKVEYVIKCDMSALQRVLYRHMQAKGVLLTDGSEKDKKGKGGTKTLMNTIM
QLRKICNHPYMFQHIEESFSEHLGFTGGIVQGLDLYRASGKFELLDRILPKLRATNHKVLLFCQMTSLMTIMEDYFAYRG
FKYLRLDGTTKAEDRGMLLKTFNEPGSEYFIFLLSTRAGGLGLNLQSADTVIIFDSDWNPHQDLQAQDRAHRIGQQNEVR
VLRLCTVNSVEEKILAAAKYKLNVDQKVIQAGMFDQKSSSHERRAFLQAILEHEEQDEEEDEVPDDETVNQMIARHEEEF
DLFMRMDLDRRREEARNPKRKPRLMEEDELPSWIIKDDAEVERLTCEEEEEKMFGRGSRHRKEVDYSDSLTEKQWLKAIE
EGTLEEIEEEVRQKKSSRKRKRDSDAGSSTPTTSTRSRDKDDESKKQKKRGRPPAEKLSPNPPNLTKKMKKIVDAVIKYK
DSSSGRQLSEVFIQLPSRKELPEYYELIRKPVDFKKIKERIRNHKYRSLNDLEKDVMLLCQNAQTFNLEGSLIYEDSIVL
QSVFTSVRQKIEKEDDSEGEESEEEEEGEEEGSESESRSVKVKIKLGRKEKAQDRLKGGRRRPSRGSRAKPVVSDDDSEE
EQEEDRSGSGSEED
>NR_148052.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NR_137288.2
MASSNPPPQPAIGDQLVPGVPGPSSEAEDDPGEAFEFDDSDDEEDTSAALGVPSLAPERDTDPPLIHLDSIPVTDPDPAA
APPGTGVPAWVSNGDAADAAFSGARHSSWKRKSSRRIDRFTFPALEEDVIYDDVPCESPDAHQPGAERNLLYEDAHRAGA
PRQAEDLGWSSSEFESYSEDSGEEAKPEVEVEPAKHRVSFQPKMTQLMKAAKSGTKDGLEKTRMAVMRKVSFLHRKDVLG
DSEEEDMGLLEVSVSDIKPPAPELGPMPEGLSPQQVVRRHILGSIVQSEGSYVESLKRILQDYRNPLMEMEPKALSARKC
QVVFFRVKEILHCHSMFQIALSSRVAEWDSTEKIGDLFVASFSKSMVLDVYSDYVNNFTSAMSIIKKACLTKPAFLEFLK
RRQVCSPDRVTLYGLMVKPIQRFPQFILLLQDMLKNTPRGHPDRLSLQLALTELETLAEKLNEQKRLADQVAEIQQLTKS
VSDRSSLNKLLTSGQRQLLLCETLTETVYGDRGQLIKSKERRVFLLNDMLVCANINFKPANHRGQLEISSLVPLGPKYVV
KWNTALPQVQVVEVGQDGGTYDKDNVLIQHSGAKKASASGQAQNKVYLGPPRLFQELQDLQKDLAVVEQITLLISTLHGT
YQNLNMTVAQDWCLALQRLMRVKEEEIHSANKCRLRLLLPGKPDK
>NR_132740.2
MGDEKDSWKVKTLDEILQEKKRRKEQEEKAEIKRLKNSDDRDSKRDSLEEGELRDHCMEITIRNSPYRREDSMEDRGEED
DSLAIKPPQQMSRKEKVHHRKDEKRKEKCRHHSHSAEGGKHARVKEREHERRKRHREEQDKARREWERQKRREMAREHSR
RERDRLEQLERKRERERKMREQQKEQREQKERERRAEERRKEREARREVSAHHRTMREDYSDKVKASHWSRSPPRPPRER
FELGDGRKPGEARPAPAQKPAQLKEEKMEERDLLSDLQDISDSERKTSSAESSSAESGSGSEEEEEEEEEEEEEGSTSEE
SEEEEEEEEEEEEETGSNSEEASEQSAEEVSEEEMSEDEERENENHLLVVPESRFDRDSGESEEAEEEVGLPERRGVPVP
EQDRGGHLWSGLQSKRQENR
>NR_037687.2
MGTRQKELLDIDSSSVILEDGITKLNTIGHYEISNGSTIKVFKKIANFTSDVEYSDDHCHLILPDSEAFQDVQGKRHRGK
HKFKVKEMYLTKLLSTKVAIHSVLEKLFRSIWSLPNSRAPFAIKYFFDFLDAQAENKKITDPDVVHIWKTNSLPLRFWVN
ILKNPQFVFDIKKTPHIDGCLSVIAQAFMDAFSLTEQQLGKEAPTNKLLYAKDIPTYKEEVKSYYKAIRDLPPLSSSEME
EFLTQESKKHENEFNEEVALTEIYKYIVKYFDEILNKLERERGLEEAQKQLLHVKVLFDEKKKCKWM
>NR_137287.2
MASSNPPPQPAIGDQLVPGVPGPSSEAEDDPGEAFEFDDSDDEEDTSAALGVPSLAPERDTDPPLIHLDSIPVTDPDPAA
APPGTGVPAWVSNGDAADAAFSGARHSSWKRKSSRRIDRFTFPALEEDVIYDDVPCESPDAHQPAGAERNLLYEDAHRAG
APRQAEDLGWSSSEFESYSEDSGEEAKPEVEVEPAKHRVSFQPKLSPDLTRLKERYARTKRDILALRVGGRDMQELKHKY
DCKMTQLMKAAKSGTKDGLEKTRMAVMRKVSFLHRKDVLGDSEEEDMGLLEVSVSDIKPPAPELGPMPEGLSPQQVVRRH
ILGSIVQSEGSYVESLKRILQDYRNPLMEMEPKALSARKCQVVFFRVKEILHCHSMFQIALSSRVAEWDSTEKIGDLFVA
SFSKSMVLDVYSDYVNNFTSAMSIIKKACLTKPAFLEFLKRRQVCSPDRVTLYGLMVKPIQRFPQFILLLQDMLKNTPRG
HPDRLSLQLALTELETLAEKLNEQKRLADQVAEIQQLTKSVSDRSSLNKLLTSGQRQLLLCETLTETVYGDRGQLIKSKE
RRVFLLNDMLVCANINFKPANHRGQLEISSLVPLGPKYVVKWNTALPQVQVVEVGQDGGTYDKDNVLIQHSGAKKASASG
QAQNKVYLGPPRLFQELQDLQKDLAVVEQITLLISTLHGTYQNLNMTVAQDWCLALQRLMRVKEEEIHSANKCRLRLLLP
GKPDK
>NR_157088.2
MADDFGFFSSSESGAPEAAEEDPAAAFLAQQESEIAGIENDEGFGAPAGSHAAPAQPGPTSGAGSEDMGTTVNGDVFQPV
HHQRVQLQTQLPIQPKDEPAHNYSSSIWHSQGQGQKGPAGLRLPTSAQILSPFP
>NR_132739.2
MGDEKDSWKVKTLDEILQEKKRRKEQEEKAEIKRLKNSDDRDSKRDSLEEGELRDHCMEITIRNSPYRREDSMEDRGEED
DSLAIKPPQQMSRKEKVHHRKDEKRKEKCRHHSHSAEGGKHARVKEREHERRKRHREEQDKARREWERQKRREMAREHSR
RERDRLEQLERKRERERKMREQQKEQREQKERERRAEERRKEREARREVSAHHRTMREDYSDKVKASHWSRSPPRPPRER
FELGDGRKPVKEEKMEERDLLSDLQDISDSERKTSSAESSSAESGSGSEEEEEEEEEEEEEGSTSEESEEEEEEEEEEEE
ETGSNSEEASEQSAEEVSEEEMSEDEERENENHLLVVPESRFDRDSGESEEAEEEVGLPERRGVPVPEQDRGGHLWSGLQ
SKRQENR
>NR_045724.2
MADDFGFFSSSESGAPEAAEEDPAAAFLAQQESEIAGIENDEGFGAPAGSHAAPAQPGPTSGAGSEDMGTTVNGDVFQPV
HHQRVQLQTQLPIQPKDEPAHNYSSSIWHSQGQGQKGPAGLRLPTSAQILSPFP
>NR_038863.2
MKSGEDGCPSPKRERICPSLFILLEPLTDWMMPVHIDEGGSSVLSLLLQMLVSSENSLTDPPRNVLPAIWLSLNPVKLTH
KINHHRMLFGFRF
>NR_168349.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRLTLFADTLYFVWQPYSPLNHLFELFRVMDIVKVRSQMCGNNNAKFKIVVSMEHEGEKHHQGSCQRKGVPIQTPR
EHSWISCKKEFEANP
>NR_168346.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCLVNGKGSLSRPQESILGSLARKNLRR
IHRVSLVMCVRPLSPSKAIISPVTCMYTSRWPEASEESQKK
>NR_168352.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRSCQRKGVPIQTPREHSWISCKKEFEANP
>NR_168351.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCLVNGKGSLSRPQESILGSLARKNLRR
IHRVSKASYFYIEGCTLTDQTMLSDVCQTSEPKQSHHIPCDLHVYIQMA
>NR_168350.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRLTLFADTLYFVWQPYSPLNHLFELFRVMDIVKVRSQMCGNNNAKFKIVVSMEHEGEKHHQGSCQRKGVPIQTPR
EHSWISCKKEFEANP
>NR_168347.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRSCQRKGVPIQTPREHSWISCKKEFEANP
>NR_168348.1
MSSVKAGTGPFHFFCDSSLASGHLDVYMQVTGDMMALLGLRGLTHITKLTLWIRLKFFLARDPRMLSWGLDRDPFPLTRR
HEVDAQ
>NR_123717.2
MPLVEVQLLLLLYTSMRSGLGKKDKEVMTDTQWKPHIVSWQTEERDVGSSASFDCKVPGFCCTFAHAHGWWEERGIAETH
RRGYRVGEKESRRANTPKEQGQLHLVSLRGTETQE
>NR_168381.1
MLHGRRLGAKATLPHPPLWEAPERGPEIVPHSPPGKEARPPWTEATRSPGRKERTHRPPCGGGRTWSPVVSGRGGISLPV
GLQC
>NR_168373.1
MWLQVRPMPRQFCTAWHMALILSLERNVAVGPASHGVKLHLLLLYSGSNLFLILVL
>NR_168385.1
MLRCLGVSGWGRKDQGTHVLRPRRGVPGRRDFRSLPSAGDLGLCRSPPGSSIRAGVLPAAPKVAWGRWGVPEGMEGPCLG
KEGFRCLWGFSAEPGSPEQTRTELPKPDREGALVASGIHVVDRESARSSPPQ
"""
	
