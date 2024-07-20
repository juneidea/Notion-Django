import Image from "next/image";
import { Poppins } from "next/font/google";
import { cn } from "@/lib/utils";

const font = Poppins({
  subsets: ["latin"],
  weight: ["400", "600"],
});

export const Logo = () => {
  return (
    <div className="hidden md:flex items-center gap-x-2">
      <Image
        src="/logo.png"
        height="54"
        width="40"
        alt="Logo"
        className="w-full h-auto dark:hidden"
      />
      <Image
        src="/logo-dark.png"
        height="54"
        width="40"
        alt="Logo"
        className="w-full h-auto hidden dark:block"
      />
      <p className={cn("font-semibold", font.className)}>Notion</p>
    </div>
  );
};
